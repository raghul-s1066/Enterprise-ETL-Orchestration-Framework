import zipfile
from pathlib import Path

ZIP_PATH = Path("/root/airflow_project/datasets/literacy.zip")
EXTRACT_TO = Path("/root/airflow_project/data/raw")

EXTRACT_TO.mkdir(parents=True, exist_ok=True)

print(f"Reading ZIP: {ZIP_PATH}")

with zipfile.ZipFile(ZIP_PATH, "r") as z:
    z.extractall(EXTRACT_TO)

print(f"Extracted files into: {EXTRACT_TO}")
print("Files:", list(EXTRACT_TO.glob("*")))