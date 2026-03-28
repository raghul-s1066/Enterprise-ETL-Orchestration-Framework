import json
import csv
from pathlib import Path

RAW_DIR = Path("/root/airflow_project/data/raw")
PROCESSED_DIR = Path("/root/airflow_project/data/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# pick latest json file
files = sorted(RAW_DIR.glob("posts_*.json"))
if not files:
    raise FileNotFoundError("No raw JSON files found in data/raw")

latest_file = files[-1]

with open(latest_file, "r") as f:
    data = json.load(f)

output_csv = PROCESSED_DIR / "posts.csv"

with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["userId", "id", "title", "body"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"Transformed {len(data)} rows into {output_csv}")