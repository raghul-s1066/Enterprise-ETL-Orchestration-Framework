Data Model (Milestone 1)
Source
API: https://jsonplaceholder.typicode.com/posts

Raw Layer
Stored as JSON
Location: data/raw/posts_YYYYMMDD_HHMMSS.json
Processed Layer
Stored as CSV
Location: data/processed/posts.csv
Final Layer (Database)
SQLite database:

Location: data/final/posts.db
Table: posts

Column	Type	Description
userId	INT	User id
id	INT	Post id (Primary Key)
title	TEXT	Post title
body	TEXT	Post content
