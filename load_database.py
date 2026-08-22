import sqlite3
import pandas as pd


# Load the scored transaction dataset
transactions = pd.read_csv("data/flagged_transactions.csv")


# Create/connect to the SQLite database
connection = sqlite3.connect("data/forensic_analytics.db")


# Load the dataframe into a SQL table
transactions.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False
)


# Verify that the data loaded correctly
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM transactions;")

row_count = cursor.fetchone()[0]

print(f"Loaded {row_count} transactions into SQLite.")


connection.close()

print("Database created successfully.")