import shutil
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Extract started")
logging.info("File copied successfully")



BASE_DIR = Path("/root/airflow_project")

INPUT_FILE = BASE_DIR / "data/processed/literacy_cleaned.csv"
OUTPUT_FILE = BASE_DIR / "data/final/literacy_final.csv"

def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(INPUT_FILE, OUTPUT_FILE)

    print("Final dataset created:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
    