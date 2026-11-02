<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Licensing and provenance inventory

Reviewed 2026-11-01.

No root project license has been selected. This change grants no general reuse permission for the exercises, CV content, reports or historical artifacts.

| Component | Evidence and licensing boundary |
|---|---|
| Project exercises, CV text and historical reports | No root license; do not infer permission or data consent. |
| ReportLab | Declared in `cv-local-generator/requirements.txt`; a version range is not a license inventory for an installed environment. |
| pandas / profiling packages | `DataAnalyticsPy/requirements.txt` declares unpinned packages; the source also falls back to `ydata_profiling`. Resolve the actual installed distributions and their notices before distributing an environment. |
| FreeCAD examples | FreeCAD is an external runtime; its license does not license this repository's scripts or models. |

## AEKR provenance has a bounded scope

The [AEKR banner notice](../assets/AEKR-BANNER-LICENSE.txt) is copied unchanged from
the AEKR project-branding scaffold. It records the MIT provenance of that upstream
scaffold and any AEKR banner copied from it. Upstream references inside that verbatim
notice describe the toolkit, not a requirement to add its handbook here. It is not a
license for unrelated project code, data, personal material or third-party marks.

The AEKR footer names the workflow used. It neither transfers copyright to AEKR nor
imports the toolkit's CC BY handbook license into this repository. Where no banner
image is present, retaining its provenance notice does not claim that an image is bundled.

## Before redistributing

Check the actual files and installed dependency versions, preserve their applicable
notices, and obtain any missing permissions. A package name, a public repository,
a passing test or a software bill of materials is not itself a grant. This is a bounded
source inventory, not an exhaustive dependency-license or ownership certification.
The [use notes](../TERMS.md) cannot override a license grant.

Reference: [GitHub's repository licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
