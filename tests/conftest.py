import os
import zipfile
import pytest

from archive_resourse import archive_files_from_dir

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
files_path = os.path.join(root_path, 'resourse', 'files')
archive_path = os.path.join(root_path, 'resourse', 'files.zip')


@pytest.fixture()
def run_func():
    archive_files_from_dir(files_path, archive_path)


@pytest.fixture()
def open_archive():
    return zipfile.ZipFile(archive_path)

