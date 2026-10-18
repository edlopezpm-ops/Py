<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Clean vacancy markup and inspect token boundaries

Call pure helpers with synthetic markup. Observe entity decoding, script/style removal and the ASCII-oriented token matcher before using its output for keyword comparisons.

Source: [clean_text](../../cv-local-generator/cv_app.py#L203) and [tokens](../../cv-local-generator/cv_app.py#L263). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-text-cleaning.py

See the complete [runnable example](../examples/cv-text-cleaning.py). It uses synthetic values and the Python standard library.

Expected result: "Python & SQL automation -> python, sql, automation; short tokens excluded".

Limit: Regex cleanup extracts text; it is not a general HTML sanitizer. The length filter omits two-character skills such as AI and C# and provides no multilingual linguistic analysis.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
