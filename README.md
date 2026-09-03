# Py

`Py` is a non-production workspace for Python learning exercises, local prototypes, data-analysis
experiments, FreeCAD scripts, and a local CV generator. The repository is intentionally
heterogeneous: it is a collection of small projects, not a single installable Python package or a
stable public API.

## Status

Experimental and maintained on a best-effort basis. Historical inputs and generated examples are
retained as part of the workspace. Review a script and its local requirements before running it;
some components require Windows, FreeCAD, pandas, or ReportLab.

## Repository areas

- `Py Scripts/` — standalone Python learning exercises.
- `DataAnalyticsPy/` — a pandas profiling experiment and its historical sample artifacts.
- `cv-local-generator/` — a local CV and cover-letter generator with its own
  [usage guide](cv-local-generator/README.md).
- `cv-local-generator/FreeCAD Hull/` and `cv-local-generator/FreeCAD_WHRackDesing/` — FreeCAD
  geometry experiments.
- `HTML5 Scripts/` and `Sicuel Scripts/` — standalone HTML and SQL experiments.

## Validation

The repository baseline uses only the Python standard library. From the repository root, run:

```shell
python3 -m unittest discover -s tests -p 'test_*.py'
```

This validation parses every Python source file, loads every JSON document, and checks that the
documented entry points and CI contract exist. It does not execute the data-profiling job, launch
the user interfaces, import FreeCAD, or claim runtime correctness for every historical exercise.

## Running the CV generator

The most complete component is `cv-local-generator`. On Windows, from the repository root:

```powershell
.\Run-CVGenerator.ps1 -Check
.\Run-CVGenerator.ps1
```

See its local README for dependency installation, web mode, desktop mode, and packaging details.

## Governance

The professionalization baseline is governed under AEKR. Changes reach the default branch through
a pull request, the required `Validation` check, and approval and merge by the configured reviewer
account against the exact validated head. The writer and reviewer are distinct technical actors
under one Human Orchestrator in Chief (HOC); this is not an independent audit.

No license has been selected for this repository. Public visibility does not grant permission to
reuse its contents.

---

Built with the **[AI Engineering Knowledge Racking (AEKR)](https://aekr.io)** workflow.
