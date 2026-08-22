import sqlite3
import pandas as pd


# Connect to the forensic analytics database
connection = sqlite3.connect("data/forensic_analytics.db")


query = """
SELECT
    transaction_id,
    customer_id,
    transaction_date,
    transaction_time,
    merchant,
    transaction_amount,
    location,
    risk_score,
    risk_level
FROM transactions
WHERE risk_level = 'High'
ORDER BY risk_score DESC, transaction_amount DESC;
"""


results = pd.read_sql_query(query, connection)


print("\nHIGH-RISK TRANSACTIONS")
print(results.to_string(index=False))
customer_risk_query = """
SELECT
    customer_id,
    COUNT(*) AS high_risk_transactions,
    SUM(transaction_amount) AS total_amount_at_risk,
    AVG(transaction_amount) AS average_high_risk_amount,
    MAX(risk_score) AS maximum_risk_score
FROM transactions
WHERE risk_level = 'High'
GROUP BY customer_id
ORDER BY total_amount_at_risk DESC;
"""

customer_risk_results = pd.read_sql_query(
    customer_risk_query,
    connection
)

print("\nCUSTOMER RISK EXPOSURE")
print(customer_risk_results.to_string(index=False))

connection.close()