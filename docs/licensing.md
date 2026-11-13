<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Licensing and provenance inventory

Reviewed 2026-11-12.

The original code and technical documentation expressly listed in [the root license scope](../LICENSE) are now available under the standard [MIT License](../LICENSES/MIT.txt). The grant is limited to that exact path list. Personal content, operational reports, third-party material and other unlisted files receive no new grant.

| Component | Evidence and licensing boundary |
|---|---|
| Listed exercise/CV implementation, tests, examples and technical notes | MIT under the authoritative [root scope index](../LICENSE); preserve the copyright and permission notice. |
| Personal CV inputs, job files, operational inputs and historical reports | Excluded from the new grant. Code licensing is not consent to reuse personal or third-party information. |
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

<!-- (kommiBo) Decision guidance and Git-backed licensing history. -->
## Reuse decisions

| Intended action | Applicable boundary |
|---|---|
| View or fork this public repository on GitHub | GitHub's platform permissions apply; they are not a general project license for off-platform distribution or reuse. |
| Reuse an exercise or CV implementation | Check the exact file in [LICENSE](../LICENSE). Listed material is MIT; unlisted material needs its own applicable permission. Generated reports and personal CV content are not included. |
| Package the CV generator or profiling environment | Apply MIT to the listed project files, inventory dependencies separately, and exclude personal inputs. The profiling tree is not part of the new grant. |
| Reuse the AEKR scaffold or banner material | Follow the scoped notice above; it does not cover unrelated project files or trademark endorsement. |

For material without an applicable grant, a permission request should identify the repository, commit, exact files, intended use
and distribution. Send that scope to [aekr@aekr.io](mailto:aekr@aekr.io) without personal
inputs or confidential attachments. A request or repository contribution is not an
approval, transfer of ownership or automatic license change.

## Licensing change record

This records changes to license-related files and their effect. Earlier documentation
updates remain historical; an actual grant or scope clarification is identified separately.

| Date | Verified change | Effect on project permissions |
|---|---|---|
| 2026-11-01 | [Initial component inventory](https://github.com/edlopezpm-ops/Py/commit/1a101ea53a0b99934b12c63937baf4e0e53f30bd) and [AEKR notice provenance](https://github.com/edlopezpm-ops/Py/commit/d680a3d34bb8b7dbb1a77553acd19d616ee3128c). | Documented existing scopes; did not add a project-wide grant. |
| 2026-11-02 | [User-responsibility terms](https://github.com/edlopezpm-ops/Py/commit/f4d60ea583664c9af969e87f913d2937f4bf580c). | Preserved existing licenses and non-waivable rights. |
| 2026-11-12, earlier update | Added reuse decisions and this source-linked record. | Documentation only; no grant was made by that earlier update. |
| 2026-11-12, owner-delegated decision | Added the exact-path root `LICENSE` and standard `LICENSES/MIT.txt`. | New MIT grant for the listed original material; excluded material and existing third-party rights are preserved. |

A future license change needs an explicit owner decision, identified files and rights,
the actual replacement text, and consistent documentation. Preserve third-party notices
and distinguish new terms from permissions already granted for earlier copies.
