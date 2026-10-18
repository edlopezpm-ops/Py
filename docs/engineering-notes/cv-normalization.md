<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Normalize a synthetic CV into the current data shape

Inspect coercion and absent fields before ranking or rendering. The normalizer builds a fresh schema-shaped dictionary from expected mappings and lists.

Source: [normalize_cv](../../cv-local-generator/cv_app.py#L168). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-normalization.py

See the complete [runnable example](../examples/cv-normalization.py). It uses synthetic values and the Python standard library.

Expected result: "schema filled; values coerced; source unchanged; zero phone becomes empty".

Limit: Normalization is not validation. A truthy nonmapping profile or malformed experience item can raise exceptions; falsy profile values such as zero become empty strings.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
