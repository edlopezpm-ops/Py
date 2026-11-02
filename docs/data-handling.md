<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Safe data handling and publication

Reviewed 2026-11-01.

This is an operator checklist for a collection of local Python, data-analysis, HTML, SQL and CV-generation experiments, not a claim that these controls
are automatically enforced by the code.

1. Use a private working copy for real CVs, experience files and job descriptions.
   Inspect `core/`, `data/`, `jobs/` and `output/pdf/` inside the CV component before
   sharing or packaging it. The packaged directory may include those files.
2. Keep the CV web listener on loopback. Loopback limits network exposure but does not
   authenticate other local processes or users. Do not publish it through a tunnel.
3. Treat the profiling console and generated HTML as derived datasets. Replace sensitive
   report values before running demonstrations; a profile is not anonymization.
4. Review a generated prompt before pasting it into any assistant. Prompt generation
   does not send it automatically, authorize paid APIs, or remove personal details.
5. Inspect both tracked and untracked outputs before a commit. A local ignore file is
   not protection for data already tracked or included in a distribution.

The code has no common retention scheduler for these heterogeneous tools. Remove
unwanted local inputs and exports yourself, including backups and downloaded copies.

## Review before publishing

Check the complete staged diff and all attachments, not just source extensions. Reject
secrets, real customer records, personal documents and unexplained binary exports.
Use synthetic reproductions in public discussions. If information is already public,
contact AEKR through [the privacy notice](../PRIVACY.md); changing the current file
does not erase Git history or third-party copies. Rotate an exposed credential through
its provider rather than relying on a later Git deletion.
