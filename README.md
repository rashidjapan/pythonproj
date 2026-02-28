# pythonproj

Learning workspace for Python exercises, examples, and small projects.

Structure:
- exercises/: small, focused practice scripts
- projects/: multi-file project ideas
- src/: source packages/modules
- notebooks/: interactive Jupyter notebooks
- docs/: notes and learning resources
- tests/: pytest-style tests
- data/: datasets for exercises
- examples/: short illustrative scripts
- scripts/: helper scripts (run, setup)

Getting started:
1. Create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies from `requirements.txt`.
3. Run exercises in `exercises/` or open notebooks in `notebooks/`.

**Package modules**

- To execute the runner as a module (preferred):
  ```powershell
  python -m src.learning_pkg.runner
  ```
- To run the same file directly (script mode):
  ```powershell
  python src\learning_pkg\runner.py
  ```
  (the code includes logic to adjust imports when executed this way)
