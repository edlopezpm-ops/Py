<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Inspect output-name cleanup before choosing a path

Observe character removal, spaces, empty input and length limits. Keep cleanup separate from destination authorization and Windows reserved-name validation.

Source: [safe_filename](../../cv-local-generator/cv_app.py#L462) and [PDF output usage](../../cv-local-generator/cv_app.py#L467). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-output-naming.py

See the complete [runnable example](../examples/cv-output-naming.py). It uses synthetic values and the Python standard library.

Expected result: "cleanup and fallback observed; capped at 80; dots and reserved CON remain".

Limit: This helper does not establish complete Windows filename validity, uniqueness, extension policy or path authorization. It preserves dots and reserved device names; the example writes no files.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
