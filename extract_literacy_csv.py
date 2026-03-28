from pathlib import Path
import shutil
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Extract started")
logging.info("File copied successfully")



BASE_DIR = Path("/root/airflow_project")

SOURCE_FILE = BASE_DIR / "datasets" / "literacy_rate_2026.csv"
RAW_DIR = BASE_DIR / "data" / "raw"
DEST_FILE = RAW_DIR / "literacy_rate_2026.csv"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {SOURCE_FILE}")

    shutil.copy(SOURCE_FILE, DEST_FILE)
    print("Extract complete. Copied to:", DEST_FILE)


if __name__ == "__main__":
    main()
    