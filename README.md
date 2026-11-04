# Lab 6 - GitHub Actions

A `Calculator` class (`calculator.py`) with `add`, `subtract`, `multiply` and `divide`,
tested with pytest (`tests/test_calculator.py`, 3 tests per method).

The workflow in `.github/workflows/ci.yml` runs all tests on every push to `master`/`main`.

Run locally: `pip install pytest && pytest -v`
