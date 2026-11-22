# Use of Generative AI – Deliverable 4

## Tools used

| Tool                            | Model           | Used for                                                                           |
| ------------------------------- | --------------- | ---------------------------------------------------------------------------------- |
| GitHub Copilot (VS Code)        | Not recorded    | Reviewing the requirements, our implementation and tests, suggesting corrections   |
| Claude Code (VS Code extension) | Claude Opus 5.5 | Checking the hand-in against the assignment, preparing the notebook and repo files |

## Summary of use

### 1. Writing and reviewing the code (Tasks 1–2)

We wrote `temperature.py`, `fraction.py`, `test_temperature.py` and `test_fraction.py` ourselves.
GitHub Copilot was used to review the deliverable requirements, inspect the implementation and tests,
find missing submission files and suggest corrections. We checked its suggestions by running the
test suite locally before keeping them.

### 2. Final check before hand-in (Claude Code, 22 Nov 2026)

We asked Claude Code: *"what needs to be done before i deliver?"* It:

- Read the assignment (`deliverable_4_assignment.pdf`), both classes, both test files and the notebook,
  and compared them with each requirement in Task 1 and Task 2.
- Ran the test suite with our virtual environment: all 37 tests passed (30 for `Temperature`,
  7 for `Fraction`). It found no problems in the classes or tests.
- Listed the missing hand-in items: `requirements.txt`, `git_log.txt`, a PDF of the notebook,
  committing the notebook, and the video.
- Pointed out that the test output in the notebook contained terminal colour codes that would show
  up as garbage text in the PDF, and that our GenAI section only mentioned Copilot.

### 3. Fixing the hand-in items (Claude Code, 22 Nov 2026)

We asked it to fix the issues it could. It did not change `temperature.py`, `fraction.py` or the test
files. It:

- Generated `requirements.txt` from our `.venv` with `pip freeze`.
- Added `--color=no` to the pytest commands in the notebook and re-ran it.
- Exported the notebook to PDF with `nbconvert` (webpdf), renamed the assignment PDF to
  `deliverable_4_assignment.pdf` so the two PDFs would not be mixed up, and committed the files.
- Tried to push to GitHub, which failed because the session had no GitHub login, so we pushed ourselves.

## Reflection

The AI tools were most useful for checking the hand-in against the assignment and doing repetitive
setup work (requirements, PDF export, git log). We wrote the code and tests ourselves and used AI
to review them; everything it suggested was checked by running the tests and reading the output
before we kept it.
