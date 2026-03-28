import json
import requests
from datetime import datetime
from pathlib import Path

RAW_PATH = Path("/root/airflow_project/data/raw")

def extract_users():
    RAW_PATH.mkdir(parents=True, exist_ok=True)

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_PATH / f"users_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(response.json(), f, indent=2)

    print(f"Saved file: {file_path}")

if __name__ == "__main__":
    extract_users()
    