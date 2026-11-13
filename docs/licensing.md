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

<!-- (kommiBo) Decision guidance and Git-backed history; no relicensing. -->
## Reuse decisions

| Intended action | Applicable boundary |
|---|---|
| View or fork this public repository on GitHub | GitHub's platform permissions apply; they are not a general project license for off-platform distribution or reuse. |
| Reuse an exercise, CV template or generated report | Identify the exact files and intended distribution, then obtain the missing project permission. Check personal information separately from copyright. |
| Package the CV generator or profiling environment | Inventory the installed dependencies and retain their notices; permission for those dependencies does not grant rights to the project or personal inputs. |
| Reuse the AEKR scaffold or banner material | Follow the scoped notice above; it does not cover unrelated project files or trademark endorsement. |

For a permission request, identify the repository, commit, exact files, intended use
and distribution. Send that scope to [aekr@aekr.io](mailto:aekr@aekr.io) without personal
inputs or confidential attachments. A request or repository contribution is not an
approval, transfer of ownership or automatic license change.

## Licensing change record

This records changes to license-related files and their effect. Documentation and
terms updates are not presented as a replacement software license.

| Date | Verified change | Effect on project permissions |
|---|---|---|
| 2026-11-01 | [Initial component inventory](https://github.com/edlopezpm-ops/Py/commit/1a101ea53a0b99934b12c63937baf4e0e53f30bd) and [AEKR notice provenance](https://github.com/edlopezpm-ops/Py/commit/d680a3d34bb8b7dbb1a77553acd19d616ee3128c). | Documented existing scopes; did not add a project-wide grant. |
| 2026-11-02 | [User-responsibility terms](https://github.com/edlopezpm-ops/Py/commit/f4d60ea583664c9af969e87f913d2937f4bf580c). | Preserved existing licenses and non-waivable rights. |
| 2026-11-12 | Added reuse decisions and this source-linked record. | Clarifies the current permission boundaries; does not relicense project material. |

A future license change needs an explicit owner decision, identified files and rights,
the actual replacement text, and consistent documentation. Preserve third-party notices
and distinguish new terms from permissions already granted for earlier copies.
