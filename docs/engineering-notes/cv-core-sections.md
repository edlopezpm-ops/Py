<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Parse synthetic core sections and skill separators

Use the recognized heading and role conventions to inspect parser behavior. The fixture uses a reserved example email and invented experience.

Source: [split_skill_line/lines_between](../../cv-local-generator/cv_app.py#L79) and [core_to_cv](../../cv-local-generator/cv_app.py#L101). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-core-sections.py

See the complete [runnable example](../examples/cv-core-sections.py). It uses synthetic values and the Python standard library.

Expected result: "three skills; one experience; one education; missing start falls back to first line".

Limit: Regex heading matching is heuristic. Missing start markers default to the beginning; company names are title-cased and skills cap at 42. Arbitrary resume layouts need separate review.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
