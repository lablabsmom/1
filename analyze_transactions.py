import pandas as pd


transactions = pd.read_csv("data/transactions.csv")

print("Dataset loaded successfully.")
print(f"Total transactions: {len(transactions)}")

print("\nColumns:")
print(transactions.columns.tolist())


# Flag unusually large transactions
transactions["large_amount_flag"] = (
    transactions["transaction_amount"] > 2500
).astype(int)

large_transactions = transactions[
    transactions["large_amount_flag"] == 1
]

print("\nLarge transactions flagged:")
print(len(large_transactions))

print(
    large_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "merchant",
            "transaction_time"
        ]
    ]
)
# Extract the hour from the transaction time
transactions["transaction_hour"] = (
    transactions["transaction_time"]
    .str.split(":")
    .str[0]
    .astype(int)
)

# Flag transactions occurring between midnight and 5 AM
transactions["odd_hour_flag"] = (
    transactions["transaction_hour"] < 5
).astype(int)

odd_hour_transactions = transactions[
    transactions["odd_hour_flag"] == 1
]

print("\nOdd-hour transactions flagged:")
print(len(odd_hour_transactions))

print(
    odd_hour_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_time",
            "transaction_amount",
            "merchant"
        ]
    ].head(20)
)
# Flag large round-dollar transactions
transactions["round_amount_flag"] = (
    (transactions["transaction_amount"] >= 1000)
    & (transactions["transaction_amount"] % 1000 == 0)
).astype(int)

round_amount_transactions = transactions[
    transactions["round_amount_flag"] == 1
]

print("\nLarge round-dollar transactions flagged:")
print(len(round_amount_transactions))

print(
    round_amount_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "transaction_time",
            "merchant"
        ]
    ]
)
# Create a full timestamp from date and time
transactions["transaction_datetime"] = pd.to_datetime(
    transactions["transaction_date"] + " " + transactions["transaction_time"]
)

# Sort transactions by customer and time
transactions = transactions.sort_values(
    by=["customer_id", "transaction_datetime"]
)
# Calculate each customer's average transaction amount
transactions["customer_avg_amount"] = (
    transactions
    .groupby("customer_id")["transaction_amount"]
    .transform("mean")
)

# Compare each transaction to the customer's average spending
transactions["amount_vs_average"] = (
    transactions["transaction_amount"]
    / transactions["customer_avg_amount"]
)

# Flag transactions that are at least 5 times the customer's average
transactions["spending_deviation_flag"] = (
    transactions["amount_vs_average"] >= 5
).astype(int)

# Calculate minutes since the customer's previous transaction
transactions["minutes_since_previous"] = (
    transactions
    .groupby("customer_id")["transaction_datetime"]
    .diff()
    .dt.total_seconds()
    / 60
)

# Flag transactions occurring within 30 minutes of the previous transaction
transactions["velocity_flag"] = (
    transactions["minutes_since_previous"] <= 30
).astype(int)

# Identify groups of closely spaced transactions
transactions["new_burst"] = (
    transactions["minutes_since_previous"].isna()
    | (transactions["minutes_since_previous"] > 30)
).astype(int)

# Give each transaction burst its own ID
transactions["burst_id"] = (
    transactions
    .groupby("customer_id")["new_burst"]
    .cumsum()
)

# Count how many transactions belong to each burst
transactions["burst_size"] = (
    transactions
    .groupby(["customer_id", "burst_id"])["transaction_id"]
    .transform("count")
)

# Flag bursts containing at least 3 transactions
transactions["burst_flag"] = (
    transactions["burst_size"] >= 3
).astype(int)

# Calculate the total transaction amount within each burst
transactions["burst_total_amount"] = (
    transactions
    .groupby(["customer_id", "burst_id"])["transaction_amount"]
    .transform("sum")
)

# Flag high-value bursts: at least 3 transactions totaling $2,500 or more
transactions["high_value_burst_flag"] = (
    (transactions["burst_size"] >= 3)
    & (transactions["burst_total_amount"] >= 2500)
).astype(int)

print("\nHigh-value burst results for planted customer C0084:")
print(
    transactions[
        transactions["transaction_id"].isin(
            ["T010006", "T010007", "T010008", "T010009"]
        )
    ][
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "burst_size",
            "burst_total_amount",
            "high_value_burst_flag"
        ]
    ].to_string(index=False)
)

velocity_transactions = transactions[
    transactions["velocity_flag"] == 1
]

print("\nHigh-velocity transactions flagged:")
print(len(velocity_transactions))

print(
    velocity_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_datetime",
            "transaction_amount",
            "minutes_since_previous"
        ]
    ].head(20)
)
print("\nVelocity results for planted customer C0025:")

print(
    transactions[
        (transactions["customer_id"] == "C0025")
        & (transactions["velocity_flag"] == 1)
    ][
        [
            "transaction_id",
            "customer_id",
            "transaction_datetime",
            "transaction_amount",
            "minutes_since_previous",
            "velocity_flag"
        ]
    ]
)

print("\nBurst results for planted customer C0084:")

print(
    transactions[
        transactions["transaction_id"].isin(
            ["T010006", "T010007", "T010008", "T010009"]
        )
    ][
        [
            "transaction_id",
            "customer_id",
            "transaction_datetime",
            "transaction_amount",
            "minutes_since_previous",
            "burst_id",
            "burst_size",
            "burst_flag"
        ]
    ]
)

# Calculate a transparent rule-based risk score
transactions["risk_score"] = (
    transactions["large_amount_flag"] * 25
    + transactions["odd_hour_flag"] * 15
    + transactions["round_amount_flag"] * 15
    + transactions["velocity_flag"] * 25
    + transactions["spending_deviation_flag"] * 20
    + transactions["burst_flag"] * 10
    + transactions["high_value_burst_flag"] * 20
)

# Assign risk categories
transactions["risk_level"] = "Low"

transactions.loc[
    transactions["risk_score"] >= 40,
    "risk_level"
] = "Medium"

transactions.loc[
    transactions["risk_score"] >= 70,
    "risk_level"
] = "High"

# Display the highest-risk transactions
highest_risk = transactions.sort_values(
    by="risk_score",
    ascending=False
)
# Review transactions with unusually high spending
deviation_transactions = transactions[
    transactions["spending_deviation_flag"] == 1
]

print("\nCustomer spending deviations flagged:")
print(len(deviation_transactions))

print(
    deviation_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "customer_avg_amount",
            "amount_vs_average",
            "spending_deviation_flag"
        ]
    ]
    .sort_values("amount_vs_average", ascending=False)
    .head(20)
)
print("\nHighest-risk transactions:")

print(
    highest_risk[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "large_amount_flag",
            "odd_hour_flag",
            "round_amount_flag",
            "velocity_flag",
            "risk_score",
            "risk_level"
        ]
    ].head(20)
)


# Evaluate the risk scoring framework against known synthetic labels
transactions["predicted_flag"] = (
    transactions["risk_score"] >= 40
).astype(int)

true_positives = len(
    transactions[
        (transactions["predicted_flag"] == 1)
        & (transactions["fraud_flag"] == 1)
    ]
)

false_positives = len(
    transactions[
        (transactions["predicted_flag"] == 1)
        & (transactions["fraud_flag"] == 0)
    ]
)

false_negatives = len(
    transactions[
        (transactions["predicted_flag"] == 0)
        & (transactions["fraud_flag"] == 1)
    ]
)

true_negatives = len(
    transactions[
        (transactions["predicted_flag"] == 0)
        & (transactions["fraud_flag"] == 0)
    ]
)

precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)

print("\nMODEL EVALUATION")
print(f"True Positives:  {true_positives}")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")
print(f"True Negatives:  {true_negatives}")
print(f"Precision:       {precision:.2%}")
print(f"Recall:          {recall:.2%}")


# Review false negatives
false_negative_transactions = transactions[
    (transactions["predicted_flag"] == 0)
    & (transactions["fraud_flag"] == 1)
]

print("\nFALSE NEGATIVES")
print(
    false_negative_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "merchant",
            "transaction_time",
            "large_amount_flag",
            "odd_hour_flag",
            "round_amount_flag",
            "velocity_flag",
            "risk_score"
        ]
    ].to_string(index=False)
)


# Review false positives
false_positive_transactions = transactions[
    (transactions["predicted_flag"] == 1)
    & (transactions["fraud_flag"] == 0)
]

print("\nFALSE POSITIVES")
print(
    false_positive_transactions[
        [
            "transaction_id",
            "customer_id",
            "transaction_amount",
            "merchant",
            "transaction_time",
            "large_amount_flag",
            "odd_hour_flag",
            "round_amount_flag",
            "velocity_flag",
            "risk_score"
        ]
    ].to_string(index=False)
)


# Save final analyzed dataset
transactions.to_csv("data/flagged_transactions.csv", index=False)

print("\nSaved scored dataset to data/flagged_transactions.csv")