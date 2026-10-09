"""Deterministically pack an extracted `artifact/` directory into artifact_bundle.tar.gz.

Usage: python3 tools/pack_artifact_bundle.py <dir containing artifact/> <output.tar.gz>

Entries are sorted, owned by uid/gid 0, stamped with a fixed mtime, and the gzip
header carries no timestamp or filename. macOS AppleDouble (`._*`), `.DS_Store`,
and `__pycache__` entries are never written, so extraction with GNU tar on Linux
yields exactly the files listed in artifact/MANIFEST.sha256.
The tar stream is byte-reproducible; the gzip bytes, and so the outer sha256,
are reproducible only with the same zlib build.
"""

from __future__ import annotations

import gzip
import io
import os
import sys
import tarfile
from pathlib import Path


MTIME = int(os.environ.get("SOURCE_DATE_EPOCH", "1790750658"))  # commit 493df8c


def skipped(path: Path) -> bool:
    return path.name.startswith("._") or path.name == ".DS_Store" or "__pycache__" in path.parts


def main() -> None:
    base, output = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
    root = base / "artifact"
    paths = [root, *sorted(path for path in root.rglob("*") if not skipped(path.relative_to(base)))]
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w", format=tarfile.USTAR_FORMAT) as archive:
        for path in paths:
            info = tarfile.TarInfo(path.relative_to(base).as_posix())
            info.mtime, info.uid, info.gid, info.uname, info.gname = MTIME, 0, 0, "", ""
            if path.is_dir():
                info.type, info.mode = tarfile.DIRTYPE, 0o755
                archive.addfile(info)
            else:
                data = path.read_bytes()
                info.size, info.mode = len(data), 0o644
                archive.addfile(info, io.BytesIO(data))
    with output.open("wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as handle:
        handle.write(buffer.getvalue())
    print(f"entries={len(paths)}")


if __name__ == "__main__":
    main()
