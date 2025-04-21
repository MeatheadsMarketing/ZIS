import shutil
from pathlib import Path
import io
import zipfile

def export_clarity_package(path: Path):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zipf:
        for file in path.rglob("*"):
            if file.is_file():
                zipf.write(file, arcname=file.relative_to(path))
    buffer.seek(0)
    return buffer