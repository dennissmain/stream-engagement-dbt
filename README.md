
# 🎬 Stream Engagement Analytics Project

Welcome to the Stream Engagement DBT Stack — a fully simulated, analytics-ready pipeline that mimics a Netflix-style user behavior tracking system. This project is designed to give data professionals a complete, hands-on walkthrough of building a data stack using **Python**, **PostgreSQL**, and **dbt**.

From generating realistic user activity (like watching, liking, pausing, and searching) to transforming raw events into meaningful insights, this repo walks you through every step.

---

## 🧠 What This Project Covers

This stack simulates a simplified streaming platform backend and demonstrates:

- 🔧 **Synthetic event generation** using Python & Faker
- 💾 **Data ingestion** into PostgreSQL or CSV
- 🧱 **Data transformation** using dbt (with staging + marts)
- 📈 **Insight-ready models** for analytics and dashboards

You’ll end up with engagement metrics like:
- Watch-to-like ratios
- Genre preferences
- Top/Bottom engaged users
- KPI tables for dashboards

---

## 🗂️ Folder Structure

```bash
stream-engagement-dbt/
├── dataset/                      # Python-based data generation
│   ├── generate_events.py        # Script to simulate 10k+ fake user events
│   └── events.csv                # Output data file (if not loading directly into SQL)
├── sql/
│   └── create_events_table.sql   # SQL schema to create the base events table
├── dbt/                          # dbt project for modeling and metrics
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/              # Clean and rename raw data
│   │   └── marts/                # Fact tables and aggregated metrics
├── requirements.txt              # Python package dependencies
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements & Setup

To get started, make sure you have the following installed:

- Python 3.8+
- PostgreSQL (locally or in Docker)
- dbt-core + dbt-postgres
- Python packages: `faker`, `pandas`, `psycopg2-binary`

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use This Project

### 📌 Step 1: Generate Fake Streaming Data

```bash
cd dataset
python generate_events.py
```

This script will create a realistic stream of user actions (watch, like, pause, etc.) with random timestamps, durations, and movie IDs.

---

### 🛠 Step 2: Load Data into PostgreSQL

You can do this in two ways:

- Run `create_events_table.sql` in `psql` or a GUI like DBeaver
- Import the `events.csv` file using any SQL import tool

---

### 🧱 Step 3: Run dbt Models

```bash
cd dbt
dbt debug        # Check your connection
dbt run          # Run all transformation models
dbt test         # Run data quality checks
dbt docs generate && dbt docs serve  # Launch interactive docs
```

---

## 📊 Models & Metrics

| Model Name             | Purpose                                 |
|------------------------|------------------------------------------|
| `stg_events`           | Cleans raw event data                   |
| `user_genre_engagement`| Aggregates user engagement by genre     |
| `fact_engagement`      | Fact table with totals and ratios       |

---

## 📈 Example KPIs You’ll Discover

- 🕒 Total Watch Time
- 👍 Total Likes
- ⚖️ Watch-to-Like Ratio
- 🎭 Most Engaged Genres
- 🚨 Bottom 50 Users by Likes

These are great for building dashboards in Tableau, Power BI, or Streamlit.

---

## 🧾 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Built as a learning project to explore modern data stack best practices — including dbt modeling, PostgreSQL warehousing, and Python-based data simulation.


