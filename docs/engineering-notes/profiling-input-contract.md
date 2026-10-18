<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Prepare a synthetic fixed-width profiling input

The profiling script reads a report and writes HTML at import time. Prepare a separate small input to review column boundaries before installing dependencies or touching historical artifacts.

Source: [ImportPandas.py paths/read_fwf/report steps](../../DataAnalyticsPy/ImportPandas.py#L11). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/profiling-input-contract.py

See the complete [runnable example](../examples/profiling-input-contract.py). It uses synthetic values and the Python standard library.

Expected result: a two-row report followed by "two synthetic rows; total units=19; profiling source not imported".

Limit: Explicit slices check this fixture only. pandas inference, ProfileReport, package fallback and HTML generation remain unexecuted. A separate pandas experiment can use read_fwf with colspecs [(0,10),(10,None)]; no historical input is needed.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
