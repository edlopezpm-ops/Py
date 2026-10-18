<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Explain keyword weighting and stable ordering

Trace phrase weights and stable ties using a fixed keyword list. Important extracted terms originate in a set, so extraction membership and extraction order require separate assertions.

Source: [extract_keywords/score_text/reorder_by_keywords](../../cv-local-generator/cv_app.py#L271). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-keyword-ranking.py

See the complete [runnable example](../examples/cv-keyword-ranking.py). It uses synthetic values and the Python standard library.

Expected result: "phrase=2; single=1; ties stable; SQL matches NoSQL; extraction deduplicated".

Limit: Substring matching does not verify a skill. Set iteration can change extraction order across processes; a short limit can select a different subset.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
