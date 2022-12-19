import os

from PyPDF2 import PdfReader
from xlrd3 import open_workbook

from tests.conftest import files_path


def test_archive(run_func, open_archive):
    with open_archive as zf:
        assert zf.testzip() is None


def test_file_list(open_archive):
    with open_archive as zf:
        assert zf.namelist() == os.listdir(files_path)


def test_csv_file(open_archive):
    with open_archive as zf:
        name = 'username.csv'
        assert zf.getinfo(name).file_size == os.path.getsize(os.path.join(files_path, name))
        z_file = zf.read(name)
        with open(os.path.join(files_path, name), 'rb') as file:
            csv_file = file.read()
            assert z_file == csv_file


def test_pdf_file(open_archive):
    with open_archive as zf:
        name = 'docs-pytest-org-en-latest.pdf'
        assert zf.getinfo(name).file_size == os.path.getsize(os.path.join(files_path, name))
        zreader = PdfReader(zf.open(name))
        reader = PdfReader(os.path.join(files_path, name))
        assert len(zreader.pages) == len(reader.pages)
        assert zreader.pages[0].extract_text() == reader.pages[0].extract_text()
        assert zreader.pages[5].extract_text() == reader.pages[5].extract_text()
        assert zreader.pages[20].extract_text() == reader.pages[20].extract_text()


def test_xls_file(open_archive):
    with open_archive as zf:
        name = 'file_example_XLS_10.xls'
        assert zf.getinfo(name).file_size == os.path.getsize(os.path.join(files_path, name))
        zbook = open_workbook(file_contents=zf.read(name))
        zsheet = zbook.sheet_by_index(0)
        book = open_workbook(os.path.join(files_path, name))
        sheet = book.sheet_by_index(0)
        assert zsheet.cell_value(rowx=5, colx=1) == sheet.cell_value(rowx=5, colx=1)
        assert [str(item) for item in zsheet.row(3)] == [str(item) for item in sheet.row(3)]
        assert [str(item) for item in zsheet.row(6)] == [str(item) for item in sheet.row(6)]
        assert [str(item) for item in zsheet.row(9)] == [str(item) for item in sheet.row(9)]
