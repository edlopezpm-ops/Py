<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Inspect source without launching applications

Use an AST inventory to separate parseable Python from executed code. Independent scripts, profiling and FreeCAD components have different requirements; importing them all is not a safe discovery technique.

Source: [repository scanner](../../tests/test_repository.py#L13) and [component map](../../README.md). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/syntax-inventory.py

See the complete [runnable example](../examples/syntax-inventory.py). It uses synthetic values and the Python standard library.

Expected result: three source paths report parse success, followed by "No application entry point executed".

Limit: AST observations do not establish dependency availability, reachable branches, UI behavior, data quality or geometry correctness.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
