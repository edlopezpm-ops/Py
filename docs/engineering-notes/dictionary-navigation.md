<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Navigate nested dictionaries and count repeated values

Use exact key paths for nested data and verify totals after aggregation. Include an explicit missing-key case before reusing the counting pattern.

Source: [BuildIns.py nested keys](../../Py%20Scripts/BuildIns.py#L17) and [frequency loop](../../Py%20Scripts/BuildIns.py#L41). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/dictionary-navigation.py

See the complete [runnable example](../examples/dictionary-navigation.py). It uses synthetic values and the Python standard library.

Expected result: "four distinct values; seven observations; v1=3; missing defaults to zero".

Limit: The original loop tests truthiness of existing counts. Positive counts work here; zero or nonnumeric initial counts require a separately specified contract.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
