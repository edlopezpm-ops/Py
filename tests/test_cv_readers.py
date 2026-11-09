# (kommiBo) Reader regressions use synthetic inputs, never personal core/job files.
from __future__ import annotations

import importlib.util
from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cv_reader_tests", ROOT / "cv-local-generator" / "cv_app.py"
)
cv_app = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cv_app)


def docx_document(body: str) -> BytesIO:
    document = BytesIO()
    with ZipFile(document, "w") as archive:
        archive.writestr(
            "word/document.xml",
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f"<w:body>{body}</w:body></w:document>",
        )
    document.seek(0)
    return document


class DocxReaderTests(unittest.TestCase):
    def test_explicit_word_separators_are_preserved(self) -> None:
        for tag, separator in (("tab", "\t"), ("br", "\n"), ("cr", "\n")):
            with self.subTest(tag=tag), docx_document(
                f"<w:p><w:r><w:t>Python</w:t><w:{tag}/><w:t>SQL</w:t></w:r></w:p>"
            ) as document:
                self.assertEqual(f"Python{separator}SQL", cv_app.read_docx(document))

    def test_adjacent_text_runs_do_not_gain_spaces(self) -> None:
        with docx_document(
            "<w:p><w:r><w:t>Py</w:t></w:r><w:r><w:t>thon</w:t></w:r></w:p>"
        ) as document:
            self.assertEqual("Python", cv_app.read_docx(document))

    def test_paragraph_tab_stop_is_not_text(self) -> None:
        with docx_document(
            '<w:p><w:pPr><w:tabs><w:tab w:val="left" w:pos="720"/>'
            "</w:tabs></w:pPr><w:r><w:t>Python</w:t></w:r></w:p>"
        ) as document:
            self.assertEqual("Python", cv_app.read_docx(document))

    def test_paragraphs_remain_separate_lines(self) -> None:
        with docx_document(
            "<w:p><w:r><w:t>Python</w:t></w:r></w:p>"
            "<w:p><w:r><w:t>SQL</w:t></w:r></w:p>"
        ) as document:
            self.assertEqual("Python\nSQL", cv_app.read_docx(document))

    def test_job_reader_keeps_separated_keywords(self) -> None:
        with tempfile.TemporaryDirectory(prefix="cv-reader-test-") as directory:
            job = Path(directory) / "synthetic.docx"
            with docx_document(
                "<w:p><w:r><w:t>Python</w:t><w:tab/><w:t>SQL</w:t>"
                "<w:br/><w:t>automation</w:t></w:r></w:p>"
            ) as document:
                job.write_bytes(document.getvalue())
            self.assertEqual("Python SQL automation", cv_app.read_job_file(job))


if __name__ == "__main__":
    unittest.main()
