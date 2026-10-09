# RuleDiff Negative-Result Technical Report

This is the public technical-report release of *When 0.99 Becomes 0.67: A Confirmatory Failure of Lexical Policy-Impact Prediction* by Chih-Kai Wang, National Taipei University of Education.

The report is not peer reviewed, accepted, or published in MLSys proceedings. It preserves the terminal confirmatory result: the frozen lexical model scored 0.9919 stratified macro-F1 on development and 0.6661 on one held-out retail packet, with 14 affected-guard false negatives. The work does not claim observed unsafe executions or a validated end-to-end safety guarantee.

## Contents

- `main.pdf`: public four-page technical report.
- `main.tex` and local style files: report source.
- `references.bib`: bibliography.
- `artifact_bundle.tar.gz`: frozen reproducibility package.
- `CITATION.cff`: public citation metadata.
- `LICENSE`: MIT license for author-created material.
- `PUBLICATION_MANIFEST.sha256`: release checksums.
- `tools/pack_artifact_bundle.py`: deterministic packer used to rebuild `artifact_bundle.tar.gz`.

## Reproduce the evidence

Extract the artifact archive, enter its `artifact` directory, and run:

```bash
python3 verify_artifact.py
```

The expected final line is `ARTIFACT_VERIFICATION_PASS`. The verifier uses Python 3.11 or newer, requires no third-party packages or network access, and recomputes all reported development and terminal private aggregates.

## Revisions

- v1.0.1: reissued `artifact_bundle.tar.gz` so the verifier passes on Python 3.12 and newer and when extracted with GNU tar. Python 3.12 changed `sum()` over floats to compensated summation, which moves the recomputed G3 stratified macro-F1 and upper bootstrap endpoint by one unit in the last place (about `1.1e-16`); the verifier now compares these with the `1e-12` absolute tolerance it already used for development scores. The v1.0.0 bundle (sha256 `3291bb5d…109a1`) also contained macOS `._*` metadata entries that broke the manifest check on Linux. Data, labels, evaluator code, and recorded results are byte-identical; only `verify_artifact.py`, the bundle `README.md`, and `MANIFEST.sha256` changed.

## Scope

The full-paper follow-up was stopped under its preregistered rule because even oracle selective routing was slower than guard-only lazy recompilation in all four dense primary regimes. This release is the frozen negative-result fallback and does not revive that rejected positive full-paper claim.
