import os.path
import zipfile


def archive_files_from_dir(dir_path, archive_path):
    with zipfile.ZipFile(archive_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in os.listdir(dir_path):
            zf.write(os.path.join(dir_path, file), arcname=file)
