<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Python engineering recipes

Reviewed baseline: 4e4bf16857ad3ed83aba2a2f876eb2c27cf11ef5. These recipes document the existing workspace and add no application behavior. Examples use synthetic values and the standard library; temporary files are named explicitly where needed.

| Area | Responsibility | Execution boundary |
| --- | --- | --- |
| [Learning scripts](../../Py%20Scripts) | Arithmetic, collections, prompts and language exploration | Some scripts print or ask for input at import time; use the individual recipe. |
| [Profiling](../../DataAnalyticsPy/ImportPandas.py) | Read a fixed-width report and write an HTML profile | Optional dependencies; historical data is outside these examples. |
| [CV source](../../cv-local-generator/cv_app.py) | Parsing, ranking, HTTP handlers and PDF generation | Pure-helper examples do not launch a server, generate PDFs or read core/job files. |
| [Baseline scanner](../../tests/test_repository.py) | Syntax, JSON and entry-point contracts | Static validation does not establish runtime behavior. |

The structure adapts provenance, responsibility maps, separate evidence denominators and bounded acceptance from [checktimecardandgivefeedback at 235a70f](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/tree/235a70f1613f9a7c19515b3a579d7539dcff6b47): [entry/provenance](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/blob/235a70f1613f9a7c19515b3a579d7539dcff6b47/00-START-HERE.md), [architecture](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/blob/235a70f1613f9a7c19515b3a579d7539dcff6b47/01-architecture-and-stack.md), [evidence limits](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/blob/235a70f1613f9a7c19515b3a579d7539dcff6b47/07-security-privacy-quality-and-evidence.md), and [review shape](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/blob/235a70f1613f9a7c19515b3a579d7539dcff6b47/09-improvement-review-guide-and-open-decisions.md). Python source remains authoritative here; no timeKER runtime claims transfer.

For review, identify the concrete input, expected behavior, source SHA, command/interpreter, observed result, negative cases and remaining unexecuted scope. Keep the three baseline tests, recipe executions, UI checks and optional profiling/FreeCAD runs as separate evidence sets. A documentation merge or local example is not user acceptance or deployment.

## Recipes

- [Inspect source without launching applications](syntax-inventory.md)
- [Trace arithmetic and truthy conditions](arithmetic-and-truthiness.md)
- [Check the shipping unit and threshold example](unit-conversion-boundary.md)
- [Navigate nested dictionaries and count repeated values](dictionary-navigation.md)
- [Observe a decorated call and its returned value](decorator-invocation.md)
- [Replay bounded confirmation and QC prompt paths](container-prompt-paths.md)
- [Compare explanatory keyword maps with the interpreter](keyword-runtime-map.md)
- [Inject a renderer and reject an empty message](greeting-dependency-injection.md)
- [Prepare a synthetic fixed-width profiling input](profiling-input-contract.md)
- [Clean vacancy markup and inspect token boundaries](cv-text-cleaning.md)
