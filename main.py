from pathlib import Path    
from datetime import datetime
import hashlib
import mimetypes



file_path = Path(input("Enter a file path: ").strip()).expanduser()

if not file_path.is_file():
    print("The file could not be found.")
else:
    details = file_path.start()

    file_type, _ = mimetypes.guess_type(file_path.name)

    hasher = hashlib.sha256()
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
        


        print(f"\nfile: {file_path.name}")
        print(f"type: {file_type or 'uknown'}")
        print(f"size: {details.st_size:,} bytes")
        print(f"last modified: {datetime.fromtimestamp(details.st_mtime)}")
        print(f"SHA-256: {hasher.hexdigest()}")
