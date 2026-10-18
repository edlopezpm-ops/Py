<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Inject a renderer and reject an empty message

Exercise the service with an alternative renderer to expose its dependency without the application entry point, logging configuration or artificial sleep.

Source: [HelloWordOverEng.py message/service classes](../../Py%20Scripts/HelloWordOverEng.py#L10). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/greeting-dependency-injection.py

See the complete [runnable example](../examples/greeting-dependency-injection.py). It uses synthetic values and the Python standard library.

Expected result: "injected: SAMPLE; console: [ES] >>> sample; empty rejected".

Limit: The protocol does not automatically enforce runtime conformance. Whitespace-only text currently passes validation because it is truthy.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
