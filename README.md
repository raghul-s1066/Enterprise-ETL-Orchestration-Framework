🧮 Enterprise Data Cleaning and ETL — Orchestration Framework Using Python
This repository contains the project files and documentation for the "Enterprise Data Cleaning and ETL" pipeline, built as part of the Infosys Virtual Internship (Springboard). The project demonstrates the design and orchestration of an enterprise-grade ETL pipeline using Apache Airflow, Python, Pandas, and Chart.js for dashboard visualization.

📘 Project Overview
The goal of this project is to build a complete ETL (Extract, Transform, Load) framework that can:

Automate data cleaning and transformation processes
Orchestrate ETL pipelines using Apache Airflow
Implement centralized logging and alerting
Visualize pipeline metrics through a real-time dashboard
The pipeline uses the Literacy Rate dataset (sourced from Kaggle) and covers extraction, transformation, loading, and monitoring stages.

🛠️ Technology Stack
Category	Tools / Technologies
Language	Python 3.9
Orchestration	Apache Airflow 2.x
Data Processing	Pandas, PySpark
Visualization / UI	HTML, CSS, JavaScript, Chart.js
Testing	Pytest
Environment	Ubuntu (WSL2), VS Code
Data Source	CSV (Kaggle - Literacy Rate Dataset)
🧩 Milestones
Milestone 1: Environment Setup & Pipeline Design
Configured Apache Airflow in Ubuntu (WSL2).
Designed 3-stage ETL pipeline architecture: Extract → Transform → Load.
Created Airflow DAGs to orchestrate the workflow.
Verified Airflow UI at localhost:8080.
Output:
✅ Airflow DAG enterprise_etl_pipeline created and scheduled @daily.

Milestone 2: Data Cleaning & Transformation
Implemented six rule-based cleaning transformations using Pandas:
Standardize column names
Remove duplicates
Handle missing values
Trim whitespace
Convert data types
Validate data (literacy rate 0–100)
Generated cleaned dataset: data/processed/literacy_cleaned.csv.
Output:
✅ Pipeline executed successfully via DAG clean_transform_load.
Average runtime: ~51 seconds.

Milestone 3: Orchestration & Monitoring
Developed dedicated monitoring DAG with:
pipeline_health_check
generate_report
send_alert_summary
Integrated centralized logging (PipelineLogger) and Airflow email alerts.
Output:
✅ monitoring_dag executed successfully with all alerts verified.

Milestone 4: Dashboards & Deployment
Built an interactive dashboard with four sections:
Overview
Pipeline Status
Data Analysis
Logs & Alerts
Deployed on 127.0.0.1:5500/dashboard.html.
Tested on 10,000 records production dataset.
Output:
✅ Dashboard deployed successfully — 90% overall success rate, 12 total DAG runs.

🧠 Key Features
Automated ETL orchestration using Airflow
Data cleaning pipeline with modular Python functions
Centralized logging and automated alerting (email/SLA callbacks)
Real-time visualization with Chart.js dashboard
Tested on large-scale (10K+) records
📂 Project Structure


Enterprise-ETL/
├── dags/
│   ├── enterprise_etl_pipeline.py
│   ├── clean_transform_load.py
│   └── monitoring_dag.py
├── data/
│   ├── raw/
│   │   └── literacy_rate.csv
│   └── processed/
│       └── literacy_cleaned.csv
├── scripts/
│   ├── extract_data.py
│   ├── transform_data.py
│   ├── load_data.py
│   ├── pipeline_logger.py
│   └── tests/
│       └── test_cleaning_rules.py
├── dashboard/
│   ├── dashboard.html
│   ├── styles.css
│   └── charts.js
├── requirements.txt
├── airflow.cfg
└── README.md
📦 Installation & Setup
Clone this repository:

bash


git clone [github.com](https://github.com/)<your-username>/Enterprise-ETL.git
cd Enterprise-ETL
Install dependencies:

bash


pip install -r requirements.txt
Initialize and start Apache Airflow:

bash


airflow db init
airflow webserver -p 8080
airflow scheduler
Access Airflow at 
localhost

Deploy the dashboard:

bash


cd dashboard
live-server
(Or open dashboard.html in any browser.)

📊 Dashboard Preview
Overview: ETL milestones & success rate
Pipeline Status: DAG execution metrics
Data Analysis: Records processed per stage
Logs & Alerts: System logs and email alerts
(Refer to screenshots in the /media folder.)

🧾 Authors
Himaja
Jagan
Raghul
🧑‍💻 Developed under Infosys Springboard Virtual Internship Program.

⚙️ License
This project is developed for educational purposes as part of Infosys Virtual Internship.
You may reuse or adapt this code for learning and personal projects with attribution.

Would you like me to tailor this README for GitHub rendering with badges (Python, Airflow, etc.) and a project logo banner? It would make it look more professional and visually attractive.
