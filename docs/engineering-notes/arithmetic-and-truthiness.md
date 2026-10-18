<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Trace arithmetic and truthy conditions

The first condition checks a numeric sum for truthiness; the later function compares that sum to a configured value. Trace the real namespace to distinguish those decisions.

Source: [Practice.py arithmetic](../../Py%20Scripts/Practice.py#L14) and [message function](../../Py%20Scripts/Practice.py#L53). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/arithmetic-and-truthiness.py

See the complete [runnable example](../examples/arithmetic-and-truthiness.py). It uses synthetic values and the Python standard library.

Expected result: "results=(2.5, 6.25, 14.5); sum=17.0; zero is false".

Limit: Top-level printing is captured in memory. The message function reads module globals and is not an independent arithmetic API.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
