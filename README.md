# Enterprise Data Cleaning and ETL Orchestration Framework

> **Infosys Springboard Virtual Internship Project**

A production-grade ETL (Extract, Transform, Load) pipeline built with Python and Apache Airflow, designed to clean, transform, and orchestrate large-scale datasets with real-time monitoring and dashboarding.
|
---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.9 |
| Orchestration | Apache Airflow 2.x |
| Data Processing | Pandas, PySpark |
| Dashboard | Streamlit / HTML + Chart.js |
| Testing | Pytest |
| Environment | Ubuntu (WSL2), VS Code |
| Data Source | CSV (Kaggle – Literacy Rate Dataset) |

---

## 📋 Project Overview

This project implements an enterprise-grade ETL framework that:
- Extracts raw data from CSV sources
- Cleans and transforms the data using rule-based logic
- Loads processed data into the final data layer
- Monitors pipelines with automated alerts and scheduling
- Visualizes pipeline health via an interactive dashboard

The dataset used is the **Global Literacy Rate dataset** from Kaggle (10,000 records).

### Data Model

| Column | Data Type | Description |
|--------|-----------|-------------|
| S.No | Integer | Serial Number (Primary Key) |
| Country | String (VARCHAR) | Name of the Country |
| Literacy Rate | Float (DECIMAL) | Literacy Rate percentage (0–100) |
| Year | Integer | Year of recorded literacy data |

---

## 🚀 Milestones

### Milestone 1 — Environment Setup & Pipeline Design

**Objective:** Configure Apache Airflow as the orchestration engine and define the overall ETL pipeline architecture.

**What We Did:**
- Installed and configured Apache Airflow on Ubuntu (WSL2)
- Designed the ETL pipeline with three core stages: Extract → Transform → Load
- Defined the high-level data model using the Literacy Rate dataset
- Created and configured Airflow DAGs to orchestrate the pipeline
- Set up extraction scripts to read data from CSV sources
- Verified the Airflow web interface at `localhost:8080`

**Output:** The `enterprise_etl_pipeline` DAG was created with three tasks — `extract_literacy_data`, `transform_literacy_data`, and `load_literacy_data` — scheduled `@daily` and verified in the Airflow UI.

---

### Milestone 2 — Data Cleaning & Transformation

**Objective:** Implement data preparation workflows, including cleaning raw data and applying transformation rules.

**What We Did:**
- Developed a rule-based cleaning engine
- Implemented data transformations using Pandas
- Applied 6 cleaning rules (see below)
- Saved the cleaned dataset to `data/processed/literacy_cleaned.csv`
- Tested the cleaning pipeline using unit tests with Pytest

**Cleaning Rules:**

| Rule | Description |
|------|-------------|
| Rule 1 | Standardizing column names — converted to lowercase with underscores |
| Rule 2 | Removing duplicate records |
| Rule 3 | Handling missing values — removed rows with null/missing values |
| Rule 4 | Removing extra whitespace from text fields |
| Rule 5 | Data type conversion — literacy rate column to numeric format |
| Rule 6 | Data validation — literacy rate values within range 0–100 |

**Output:** The `clean_transform_load` DAG executed with 2 successful runs (mean duration: 51 seconds). Cleaned dataset saved to the processed data layer.

---

### Milestone 3 — Orchestration & Monitoring

**Objective:** Add Airflow DAGs for orchestration and integrate monitoring tools into the ETL pipeline.

**What We Did:**
- Created `monitoring_dag` with three tasks: `pipeline_health_check`, `generate_report`, and `send_alert_summary`
- Configured `@daily` DAG scheduling for automated execution
- Integrated centralized logging using the `PipelineLogger` utility module
- Implemented `on_success_callback` and `on_failure_callback` alert configurations
- Verified monitoring DAG with 2 successful runs

**Alert Configuration:**

| Alert | Trigger |
|-------|---------|
| `on_success_callback` | Pipeline completes successfully |
| `on_failure_callback` | Pipeline encounters an error |
| SLA Miss Alert | Pipeline exceeds defined time limit |
| SMTP | Configured in `airflow.cfg` for email notifications |

**Output:** The `monitoring_dag` executed with 2 successful runs (mean duration: 1 min 18 sec). Alert system verified as operational.

---

### Milestone 4 — Dashboards & Deployment

**Objective:** Build an interactive monitoring dashboard and finalize deployment of the complete ETL framework.

**What We Did:**
- Built an Enterprise ETL Pipeline Dashboard with four sections: Overview, Pipeline Status, Data Analysis, and Logs & Alerts
- Deployed the dashboard at `127.0.0.1:5500/dashboard.html`
- Tested the complete ETL pipeline on 10,000 production records
- Verified all 4 milestones as complete on the dashboard

**Output:**

| Metric | Value |
|--------|-------|
| Milestones Completed | 4 / 4 |
| Overall Success Rate | 90% |
| Total DAGs | 3 |
| Total Runs | 12 |
| Records Extracted | 10,000 |
| Records After Cleaning | ~9,500 |

---

## 📁 Project Structure

```
├── dags/
│   ├── enterprise_etl_pipeline.py
│   ├── clean_transform_load.py
│   └── monitoring_dag.py
├── data/
│   ├── raw/
│   └── processed/
│       └── literacy_cleaned.csv
├── scripts/
│   └── pipeline_logger.py
├── tests/
│   └── test_cleaning_pipeline.py
├── dashboard/
│   └── dashboard.html
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9+
- Ubuntu / WSL2
- Apache Airflow 2.x

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/etl-orchestration-framework.git
cd etl-orchestration-framework

# Install dependencies
pip install apache-airflow pandas pyspark streamlit pytest sqlalchemy

# Initialize Airflow
airflow db init
airflow users create --username admin --password admin \
  --firstname Admin --lastname User --role Admin --email admin@example.com

# Start Airflow
airflow webserver --port 8080 &
airflow scheduler &
```

### Running the Pipeline

```bash
# Trigger ETL pipeline manually
airflow dags trigger enterprise_etl_pipeline

# Trigger cleaning & transformation
airflow dags trigger clean_transform_load

# Trigger monitoring
airflow dags trigger monitoring_dag
```

---

## 📊 Dashboard

Open `dashboard/dashboard.html` with a live server (e.g., VS Code Live Server) at `127.0.0.1:5500/dashboard.html` to view:
- Overall pipeline health
- DAG run results and success rates
- Records processed per stage
- Live logs and alert configuration

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 License

This project was developed as part of the **Infosys Springboard Virtual Internship** program.
