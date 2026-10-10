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

## HOC review note — 2026-10-09

At the HOC's request, this note records Friday's maintenance review in repository history. The date uses America/New_York.

Automated baseline validation passed at [`44f9846896ff`](https://github.com/edlopezpm-ops/Py/commit/44f9846896ffa7e8f4d1a47a5ae8e1dd351e14b6). The enabled documentation maintenance rules returned `NO_ACTION`: no eligible change was found.

The check covered Python syntax, JSON parsing and documented entry points; it did not launch the individual applications.

<details>
<summary>67 test · Friday lab 🤖</summary>

(kommiBo) HOC-requested, one-off contribution-count experiment for 2026-10-09 (America/New_York). These are jokes, not additional test cases or engineering review evidence. Operator-assisted delivery; the scheduled maintenance rules are unchanged.

- 01. 🐍 The snake requested a Friday sssstand-up. — kommiBo 🤖
- 02. 📦 Imports have baggage; this note travels light. — kommiBo 🤖
- 03. ☕ Python runs on indentation and alleged coffee. — kommiBo 🤖
- 04. 🔎 ast.parse can read the room, but it does not run it. — kommiBo 🤖
- 05. 🧪 JSON brought matching brackets to the dress code. — kommiBo 🤖
- 06. 🦆 The rubber duck has declined another status meeting. — kommiBo 🤖
- 07. 🏁 Return weekend; finally, relax. — kommiBo 🤖

</details>
