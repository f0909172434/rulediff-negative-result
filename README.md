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

## Reproduce the evidence

Extract the artifact archive, enter its `artifact` directory, and run:

```bash
python3 verify_artifact.py
```

The expected final line is `ARTIFACT_VERIFICATION_PASS`. The verifier uses Python 3.11 or newer, requires no third-party packages or network access, and recomputes all reported development and terminal private aggregates.

## Scope

The full-paper follow-up was stopped under its preregistered rule because even oracle selective routing was slower than guard-only lazy recompilation in all four dense primary regimes. This release is the frozen negative-result fallback and does not revive that rejected positive full-paper claim.
