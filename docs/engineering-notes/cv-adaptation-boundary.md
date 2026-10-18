<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Inspect adaptation without writing files or inventing skills

Adapt an invented base CV in memory. Check immutability, promotion of existing matching skills and preservation of existing bullet text, then inspect generated-summary effects on analysis.

Source: [adapt_cv/build_summary](../../cv-local-generator/cv_app.py#L303). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-adaptation-boundary.py

See the complete [runnable example](../examples/cv-adaptation-boundary.py). It uses synthetic values and the Python standard library.

Expected result: "SQL promoted; existing content preserved; base unchanged; summary affects missing-keyword analysis".

Limit: The generated summary inserts vacancy keywords before missing_keywords is computed. Absence from the missing list does not establish that the original CV contained a skill. No PDF or real candidate is involved.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
