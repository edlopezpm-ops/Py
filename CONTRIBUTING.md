# Contributing to Py

<!-- (kommiBo) Repository-specific contribution and validation guidance. -->

## Propose one reproducible improvement

Identify the component and file: Python exercises, profiling, the CV generator or a
FreeCAD example have different runtimes. Include the commit, operating system, runtime
version, exact command, expected result and observed result. Use synthetic examples;
do not attach a real CV, job application, profiling export or credentials to a public issue.
Send security-sensitive reports through [SECURITY.md](SECURITY.md).

Files expressly listed in [LICENSE](LICENSE) are available under the standard
[MIT License](LICENSES/MIT.txt), without a separate approval or website-terms
condition. Check the scope before reusing other material: personal inputs and reports
are excluded. Submit only material you are authorized to provide. This guide creates
no additional contributor agreement; see the [licensing inventory](docs/licensing.md)
and [use boundaries](TERMS.md).

## Validate the affected component

From the repository root, with Python 3.12 as used by CI:

```shell
python3 -m unittest discover -s tests -p 'test_*.py'
```

The suite parses Python, loads JSON, checks documented entry points and exercises CV
readers with synthetic documents. It does not launch the CV UI, execute profiling or
validate FreeCAD geometry. A change in one of those components needs a focused check
in its actual runtime, with a sanitized output and the environment recorded. Use the
[CV guide](cv-local-generator/README.md) for that component's launch requirements.

For a Markdown-only change, check relative links and source claims; do not describe a
passing syntax check as proof that a UI or generated report works. A bug fix should
include a regression test that reproduces the defect before the fix.

## Submit a reviewable change

Keep the diff limited to the stated problem. Include the commands run, their results,
checks you could not run and any generated artifacts affected. Exclude personal inputs,
local environments and generated private reports. Changes reach the default branch
through the existing PR, validation and separate-review process. Recover a merged
change with a reviewed revert PR, preserving unrelated work.
