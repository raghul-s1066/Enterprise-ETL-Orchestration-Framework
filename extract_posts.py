import json
import requests
from datetime import datetime
from pathlib import Path

RAW_DIR = Path("/root/airflow_project/data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
response.raise_for_status()

data = response.json()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = RAW_DIR / f"posts_{timestamp}.json"

with open(output_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(data)} records to {output_file}")
