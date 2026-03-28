import csv
import sqlite3
from pathlib import Path

DB_PATH = Path("/root/airflow_project/data/final/posts.db")
CSV_PATH = Path("/root/airflow_project/data/processed/posts.csv")

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

if not CSV_PATH.exists():
    raise FileNotFoundError("posts.csv not found. Run transform first.")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS posts (
    userId INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT
)
""")

cur.execute("DELETE FROM posts")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = [(r["userId"], r["id"], r["title"], r["body"]) for r in reader]

cur.executemany(
    "INSERT INTO posts (userId, id, title, body) VALUES (?, ?, ?, ?)",
    rows
)

conn.commit()
conn.close()

print(f"Loaded {len(rows)} rows into {DB_PATH}")