<!-- (kommiBo) Source-reviewed learning recipe; synthetic examples only. -->
# Read synthetic text, CSV and DOCX with the adapters

Create temporary files with known text and a minimal DOCX ZIP member. Verify extraction and the explicit legacy DOC rejection without opening the jobs directory.

Source: [read_docx/read_csv_text/read_job_file](../../cv-local-generator/cv_app.py#L212). The example follows the checked-in implementation; it does not change that implementation.

Run from the repository root:

    python docs/examples/cv-file-readers.py

See the complete [runnable example](../examples/cv-file-readers.py). It uses synthetic values and the Python standard library.

Expected result: "TXT, CSV and DOCX extracted; DOC rejected; temporary files removed".

Limit: DOCX extraction reads paragraph text from word/document.xml only. It does not preserve layout, headers or tracked edits. This minimal ZIP is a parser fixture, not Word interoperability evidence.

For review evidence, record the repository SHA, Python version, command, exit status and observed output. A passing example establishes only the behavior asserted here. See the [source and review map](README.md).
