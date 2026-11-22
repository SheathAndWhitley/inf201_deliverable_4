# INF201 – Deliverable 4: Temperatures and Fractions

Two small classes built with special (dunder) methods, each tested with `pytest`.

Repository: <https://github.com/SheathAndWhitley/inf201_deliverable_4>

## Contents

| File | Description |
|---|---|
| `temperature.py` | `Temperature` – value in °C, °F or K, conversions, cross-unit comparisons |
| `test_temperature.py` | `pytest` tests for `Temperature` |
| `fraction.py` | `Fraction` – reduced fraction of two integers, comparisons and arithmetic |
| `test_fraction.py` | `pytest` tests for `Fraction` |
| `deliverable_4.ipynb` / `.pdf` | Presentation of both classes, with test output |
| `GenAI_Use.md` | Discussion of generative AI use |
| `git_log.txt` | Commit log |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v
```

Then open `deliverable_4.ipynb` and select the `.venv` kernel.
