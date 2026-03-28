ETL Pipeline Design (Airflow)
Pipeline Name
etl_posts_pipeline

Tasks
extract_posts

Downloads posts from API
Saves raw JSON to data/raw/
transform_posts

Converts latest JSON file to CSV
Saves CSV to data/processed/posts.csv
load_posts

Loads CSV into SQLite database
Saves DB to data/final/posts.db
DAG Flow
extract_posts → transform_posts → load_posts