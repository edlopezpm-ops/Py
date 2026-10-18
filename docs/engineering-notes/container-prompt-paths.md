<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Replay bounded confirmation and QC prompt paths

Supply a complete finite transcript to the actual interactive script. Cover retry after invalid input, direct confirmation and QC confirmation separately.

Source: [Practice2.py prompt loop](../../Py%20Scripts/Practice2.py#L26). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/container-prompt-paths.py

See the complete [runnable example](../examples/container-prompt-paths.py). It uses synthetic values and the Python standard library.

Expected result: "direct: confirmed", "retry: confirmed", and "qc: confirmed" on separate lines.

Limit: Only three finite transcripts are covered. isdigit accepts more than ASCII digits; eight characters do not prove an industry container identifier. No logistics system is contacted.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
