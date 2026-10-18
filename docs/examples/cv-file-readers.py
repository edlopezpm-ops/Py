# (kommiBo) Synthetic documentation example; no personal records.
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from _cv_source import cv
with TemporaryDirectory(prefix='py-docs-synthetic-') as directory:
    root = Path(directory)
    text = root / 'sample.txt'
    text.write_text('Python\nSQL', encoding='utf-8')
    csv = root / 'sample.csv'
    csv.write_text('skill,level\nSQL,example\n', encoding='utf-8-sig')
    docx = root / 'sample.docx'
    with ZipFile(docx, 'w') as archive:
        archive.writestr('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Synthetic SQL role</w:t></w:r></w:p></w:body></w:document>')
    assert cv.read_job_file(text) == 'Python SQL'
    assert cv.read_job_file(csv) == 'skill level SQL example'
    assert cv.read_job_file(docx) == 'Synthetic SQL role'
    try:
        cv.read_job_file(root / 'unsupported.doc')
    except ValueError:
        pass
    else:
        raise AssertionError('Legacy DOC should be rejected')
print('TXT, CSV and DOCX extracted; DOC rejected; temporary files removed')
