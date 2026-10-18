<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Interpret the bounded lexical fit score

Compare complete overlap, no overlap and an empty vacancy. This is a bounded keyword-coverage heuristic with recommendation thresholds, not a calibrated hiring probability.

Source: [assess_fit](../../cv-local-generator/cv_app.py#L353). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-fit-score.py

See the complete [runnable example](../examples/cv-fit-score.py). It uses synthetic values and the Python standard library.

Expected result: "complete=96/Proceed; absent=8/Pause; empty vacancy=8 with no keywords".

Limit: The floor is 8 and ceiling 96; recommendations use thresholds 72 and 48. Qualifications, eligibility and recruiter decisions are outside lexical overlap.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
