<!-- (kommiBo) Operator-assisted maintenance; source-reviewed documentation. -->
# Python workspace: change boundaries and recovery

| Area | Source and review boundary |
| --- | --- |
| Learning exercises | `Py Scripts/`; inspect one exercise's imports and effects before running it. |
| CV generator | `cv-local-generator/` and the root PowerShell launcher; keep web, desktop, and packaging behavior distinct. |
| Data analysis | `DataAnalyticsPy/`; inspect dependencies and input paths locally without copying historical data into issues or PR evidence. |
| Geometry | FreeCAD directories below `cv-local-generator/`; syntax validation is not geometry validation. |
| HTML and SQL | `HTML5 Scripts/` and `Sicuel Scripts/`; the Python baseline does not execute them. |

Do not regenerate historical `.rpt` or HTML outputs to validate a documentation change. A recovery for one component should not overwrite another component's artifacts.

## Recover through a reviewed PR

1. Read the current default branch and preserve the failing PR URL, its head SHA, and the relevant CI log. Distinguish an infrastructure failure from a changed project contract.
2. Create a separate recovery branch from the latest default branch. Inspect the original change and later dependent commits before choosing a corrective edit or `git revert`.
3. For a squash commit, revert that commit on the recovery branch. For a merge commit, inspect its parents and deliberately select the mainline; do not blindly copy a `-m` value. Resolve conflicts explicitly and preserve unrelated later work.
4. Run the [repository validation](validation-guide.md), inspect the diff, and open a recovery PR. Record the reason and the original PR/commit it compensates for.
5. Require the configured CI and separate reviewer approval on the current head. If the head changes, verify its checks and review again. Merge through the normal branch rules without bypass.
6. Verify the merge SHA on GitHub and the resulting default-branch validation. A successful local command or PR creation is not proof of merge completion.

Do not force-push the default branch or delete pre-existing files as a recovery shortcut. If kommiBo reports an uncertain effect, preserve its operation/run identity and reconcile it before submitting duplicate work. Writer and reviewer accounts are separate technical actors under one HOC; this is not an independent audit.
