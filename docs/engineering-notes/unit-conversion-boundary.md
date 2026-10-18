<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Check the shipping unit and threshold example

Translate the selected unit before evaluating the strict greater-than-100 threshold. Keep this pedagogical rate separate from a commercial tariff.

Source: [Practice.py unit map and shipment branch](../../Py%20Scripts/Practice.py#L105). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/unit-conversion-boundary.py

See the complete [runnable example](../examples/unit-conversion-boundary.py). It uses synthetic values and the Python standard library.

Expected result: "800 units -> 160.0; 100 -> 0; 110 -> 22.0; unknown unit rejected".

Limit: The helper reproduces the branch using the actual map and rate. It is not a weight conversion, money implementation or freight quote.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
