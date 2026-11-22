# Use of Generative AI – Deliverable 4

## Tools used

| Tool                            | Model           | Used for                                                                    |
| ------------------------------- | --------------- | --------------------------------------------------------------------------- |
| GitHub Copilot (VS Code)        | *TODO*          | Reviewing the requirements, the implementation and the tests                |
| Claude Code (VS Code extension) | Claude Opus 5.5 | Checking the hand-in against the assignment, preparing the repository files |

## Summary of use

### 1. Writing the code (Tasks 1–2)

*TODO – describe how (or whether) AI was used while writing `temperature.py`, `fraction.py`
and the two test files.*

GitHub Copilot was used to review the deliverable requirements, inspect the implementation and tests,
identify missing submission files and suggest corrections. We checked its suggestions by running the
test suite locally.

### 2. Final check before hand-in (Claude Code, 22 Nov 2026)

We asked Claude Code to compare the repository with the assignment (`deliverable_4_assignment.pdf`)
and tell us what was missing. It read the classes, tests and notebook, ran the tests (37 passed) and
listed the missing hand-in items: `requirements.txt`, `git_log.txt`, a PDF of the notebook, the
uncommitted notebook and the video. It did not change `temperature.py`, `fraction.py` or the test files.

### 3. Preparing the repository for hand-in (Claude Code, 22 Nov 2026)

We then asked Claude Code to fix what it could. It:

- Generated `requirements.txt` from our `.venv` (`pip freeze`) and added `ipykernel` so the notebook
  runs on the project's own environment.
- Rewrote `deliverable_4.ipynb` in the same format as our Deliverable 3 notebook: a short design
  description of each class, examples of each class in use and the `pytest` output. It turned off
  pytest's coloured output so the PDF doesn't show colour codes.
- Exported the notebook to `deliverable_4.pdf` (nbconvert webpdf).
- Wrote `README.md` and drafted this file. The parts about our own earlier work are marked *TODO*,
  since the assistant had no record of them.
- Generated `git_log.txt`.
