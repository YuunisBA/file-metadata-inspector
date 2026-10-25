from pathlib import Path    
from datetime import datetime
import hashlib
import mimetypes
import json


baseline_file = Path("file_hashes.json")

if baseline_file.exists():
    baseline = json.loads(baselines_file.read_text())
else:
    baselines = {}


file_path = Path(input("Enter a file path: ").strip()).expanduser()

if not file_path.is_file():
    print("The file could not be found.")
else:
    details = file_path.stat()

    file_type, _ = mimetypes.guess_type(file_path.name)

    hasher = hashlib.sha256()
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

            current_hash = hasher.hexdigest()
            file_key = str(file_path.resolve())
            previous_hash = baselines.get(file_key)


            if previous_hash is None:
                print("first scan: saves baseline hash.")
            elif previous_hash == current_hash:
                print("no change since last scan.")
            else:
                print("change has been detected since last scan")


                baselines[file_key] = current_hash
                baselines_file.write_text(json.dumps(baselines, indent=2))


        print(f"\nfile: {file_path.name}")
        print(f"type: {file_type or 'uknown'}")
        print(f"size: {details.st_size:,} bytes")
        print(f"last modified: {datetime.fromtimestamp(details.st_mtime)}")
        print(f"SHA-256: {hasher.hexdigest()}")
