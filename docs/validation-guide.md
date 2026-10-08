<!-- (kommiBo) Operator-assisted maintenance; source-reviewed documentation. -->
# Python workspace: validation and diagnosis

Run from the repository root:

```shell
python3 -m unittest discover -s tests -p 'test_*.py'
```

The baseline in [test_repository.py](../tests/test_repository.py) parses Python with `ast.parse`, decodes JSON, and checks the documented entry points. It uses the standard library; installing every component's dependencies is unnecessary for this check.

| Failure | Diagnose before changing anything |
| --- | --- |
| Python syntax error | Read the failing subtest path and line, then inspect that source with Python 3.12, matching CI. A parse success does not execute imports. |
| JSON decoding error | Inspect the named JSON document for syntax and encoding. Preserve the original input before editing it. |
| Missing entry point | Compare the reported path with the tracked tree; restore an accidental removal or update the contract together with an intentional move. |
| Local-only failure | Use a clean clone. The scanner visits local Python and JSON files except `.git`, `.venv`, `venv`, and `__pycache__`; unrelated generated files can participate. |

The baseline does not launch the CV applications, run pandas profiling, exercise PowerShell, or execute the FreeCAD models. For the CV component, follow its [own instructions](../cv-local-generator/README.md) and validate the changed execution mode separately.

See [change and recovery guidance](change-recovery.md) before merging a correction.
