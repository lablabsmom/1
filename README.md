# Fraud Risk & Transaction Monitoring Dashboard

A forensic analytics project that uses Python, SQL, Power BI, and generative AI to identify suspicious transaction patterns, assess fraud risk, and support transaction investigations.

![Fraud Risk & Transaction Monitoring Dashboard](fraud%20risk%20transaction%20monitoring.png)

## Project Overview

This project simulates a fraud risk and transaction monitoring workflow used in forensic analytics and financial investigations. Transaction data is analyzed to identify unusual activity, assign risk levels, and surface potentially suspicious transactions for further investigation.

The final Power BI dashboard provides an interactive view of transaction risk, allowing users to examine high- and medium-risk activity by customer and merchant.

## Key Features

- Transaction risk classification into Low, Medium, and High risk
- Identification of potentially suspicious transactions
- Customer-level analysis of flagged transaction value
- Merchant-level analysis of flagged transaction value
- Investigation table for reviewing individual flagged transactions
- Interactive Power BI risk-level filtering
- Risk scoring and transaction monitoring
- Visual comparison of transaction volume and monetary exposure by risk level

## Tools & Technologies

- **Power BI** — Interactive dashboard development and data visualization
- **Python** — Data analysis and fraud-risk logic
- **SQL** — Transaction querying and analysis
- **Generative AI** — Development support, analytical exploration, and workflow refinement

## Dashboard

The dashboard includes:

- Total transaction volume
- High-risk transaction count
- Medium-risk transaction count
- Transaction risk distribution
- Transaction value at risk
- Flagged transaction value by customer
- Flagged transaction value by merchant
- Transaction-level investigation table
- Interactive risk-level slicer

## Repository Contents

- `Fraud Risk & Transaction Monitoring Dashboard.pbix` — Interactive Power BI fraud risk and transaction monitoring dashboard
- `fraud risk transaction monitoring.png` — Preview image of the completed Power BI dashboard
- `analyze_transactions.py` — Python script for transaction analysis, risk scoring, and fraud flagging
- `generate_data.py` — Generates synthetic transaction data for fraud analytics testing
- `load_database.py` — Loads transaction data into the SQLite database for analysis
- `run_queries.py` — Executes investigative SQL queries against the transaction database
- `investigative_queries.sql` — SQL queries for identifying and investigating suspicious transaction patterns
- `transactions.csv` — Synthetic transaction dataset used as the analytical input
- `flagged_transactions.csv` — Output dataset containing transactions identified for further investigation
- `README.md` — Project overview, methodology, technologies, and documentation
- 
## Purpose

This project was developed as a portfolio demonstration of forensic analytics, fraud risk analysis, data visualization, and technology-enabled investigation techniques.
