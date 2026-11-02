<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Privacy — Py

Reviewed 2026-11-01.

## Scope and responsibility

AEKR maintains this project's notices and is the contact for questions at
[aekr@aekr.io](mailto:aekr@aekr.io). This notice covers a collection of local Python, data-analysis, HTML, SQL and CV-generation experiments.
It does not claim a new legal entity or apply the aekr.io website's analytics,
questionnaire, browser-data email service or retention periods to this repository.

## What the reviewed source does

The CV application reads local profile, core-experience and job files and writes PDFs
under `cv-local-generator/output/pdf/`. Its web server binds to `127.0.0.1`;
browser requests to that server are local processing, not an upload to AEKR.
The desktop application uses the same local generator. A generated prompt can be
copied into another tool manually; that separate disclosure is the user's decision.

`DataAnalyticsPy/ImportPandas.py` reads a historical shipment report, prints dataframe
information and writes an HTML profile. Inputs, console output and the HTML can contain
source values. Historical reports, CV material and generated files must not be assumed
fictional, anonymous, or cleared for redistribution merely because they are committed.

Source evidence: [CV server](cv-local-generator/cv_app.py), [desktop UI](cv-local-generator/desktop_app.py), [profiling script](DataAnalyticsPy/ImportPandas.py). This is a source review, not a guarantee about every
dependency, host, historical artifact or future deployment.

## Hosting, requests and retention

GitHub processes repository visits and collaboration activity under its
[privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
If you serve a local copy over HTTP, that server can log requests. Downloading runtimes
or dependencies contacts their providers. Those operations are distinct from collection
implemented by the project itself. No repository-wide anonymous-visitor or zero-log
guarantee is made here.

Public issues, commits and attachments can be retained in history, forks, caches and
clones. Do not submit secrets, personal records or confidential data. For questions,
corrections, access or removal requests about project-held information, contact AEKR;
use [SECURITY.md](SECURITY.md) for a vulnerability report. Requests are considered under
applicable requirements; this notice promises neither a specific legal outcome nor
deletion of copies controlled by other parties. Local files have the retention described
in the [data-handling guide](docs/data-handling.md).
