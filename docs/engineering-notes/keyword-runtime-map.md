<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Compare explanatory keyword maps with the interpreter

Read literal dictionaries through the AST instead of importing an interactive script. Compare maintained vocabulary with the current interpreter and distinguish soft keywords.

Source: [SampleKeywords.py](../../Py%20Scripts/SampleKeywords.py#L5) and [MasterPyKWs.py](../../Py%20Scripts/MasterPyKWs.py#L7). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/keyword-runtime-map.py

See the complete [runnable example](../examples/keyword-runtime-map.py). It uses synthetic values and the Python standard library.

Expected result: the reserved/soft distinction plus an interpreter-dependent list of unexplained reserved keywords.

Limit: These dictionaries are learning material. Keyword totals can change across Python versions; record the actual interpreter instead of hard-coding an historical count.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
