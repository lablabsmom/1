import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)

customers = [f"C{str(i).zfill(4)}" for i in range(1, 101)]

merchants = [
    "Walmart",
    "Target",
    "Starbucks",
    "Amazon",
    "Shell",
    "Publix",
    "Best Buy",
    "PetSmart",
    "Home Depot",
    "CVS"
]

locations = [
    "Atlanta GA",
    "Marietta GA",
    "Jonesboro GA",
    "Savannah GA",
    "Miami FL",
    "Charlotte NC"
]

payment_methods = [
    "Credit Card",
    "Debit Card"
]

transactions = []

start_date = datetime(2026, 1, 1)
for i in range(1, 10001):
    customer = random.choice(customers)
    merchant = random.choice(merchants)
    location = random.choice(locations)
    payment_method = random.choice(payment_methods)

    transaction_amount = round(random.uniform(5, 500), 2)

    random_days = random.randint(0, 89)
    random_hours = random.randint(6, 23)
    random_minutes = random.randint(0, 59)

    transaction_datetime = (
        start_date
        + timedelta(days=random_days)
        + timedelta(hours=random_hours, minutes=random_minutes)
    )

    account_age_days = random.randint(30, 2000)

    transactions.append({
        "transaction_id": f"T{str(i).zfill(6)}",
        "customer_id": customer,
        "transaction_date": transaction_datetime.strftime("%Y-%m-%d"),
        "transaction_time": transaction_datetime.strftime("%H:%M"),
        "merchant": merchant,
        "transaction_amount": transaction_amount,
        "location": location,
        "payment_method": payment_method,
        "account_age_days": account_age_days,
        "fraud_flag": 0
    })

suspicious_transactions = [
    # Scenario 1: Repeated large late-night transactions
    {
        "transaction_id": "T010001",
        "customer_id": "C0025",
        "transaction_date": "2026-03-15",
        "transaction_time": "02:03",
        "merchant": "Electronics Store",
        "transaction_amount": 5000.00,
        "location": "Miami FL",
        "payment_method": "Credit Card",
        "account_age_days": 420,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010002",
        "customer_id": "C0025",
        "transaction_date": "2026-03-15",
        "transaction_time": "02:09",
        "merchant": "Electronics Store",
        "transaction_amount": 5000.00,
        "location": "Miami FL",
        "payment_method": "Credit Card",
        "account_age_days": 420,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010003",
        "customer_id": "C0025",
        "transaction_date": "2026-03-15",
        "transaction_time": "02:16",
        "merchant": "Electronics Store",
        "transaction_amount": 5000.00,
        "location": "Miami FL",
        "payment_method": "Credit Card",
        "account_age_days": 420,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010004",
        "customer_id": "C0025",
        "transaction_date": "2026-03-15",
        "transaction_time": "02:22",
        "merchant": "Electronics Store",
        "transaction_amount": 5000.00,
        "location": "Miami FL",
        "payment_method": "Credit Card",
        "account_age_days": 420,
        "fraud_flag": 1
    },

    # Scenario 2: Single very large transaction during normal hours
    {
        "transaction_id": "T010005",
        "customer_id": "C0068",
        "transaction_date": "2026-02-18",
        "transaction_time": "14:35",
        "merchant": "Luxury Retail",
        "transaction_amount": 7500.00,
        "location": "Atlanta GA",
        "payment_method": "Credit Card",
        "account_age_days": 980,
        "fraud_flag": 1
    },

    # Scenario 3: Rapid sequence of smaller transactions
    {
        "transaction_id": "T010006",
        "customer_id": "C0084",
        "transaction_date": "2026-01-28",
        "transaction_time": "18:02",
        "merchant": "Online Marketplace",
        "transaction_amount": 820.40,
        "location": "Charlotte NC",
        "payment_method": "Debit Card",
        "account_age_days": 260,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010007",
        "customer_id": "C0084",
        "transaction_date": "2026-01-28",
        "transaction_time": "18:08",
        "merchant": "Online Marketplace",
        "transaction_amount": 910.25,
        "location": "Charlotte NC",
        "payment_method": "Debit Card",
        "account_age_days": 260,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010008",
        "customer_id": "C0084",
        "transaction_date": "2026-01-28",
        "transaction_time": "18:14",
        "merchant": "Online Marketplace",
        "transaction_amount": 760.90,
        "location": "Charlotte NC",
        "payment_method": "Debit Card",
        "account_age_days": 260,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010009",
        "customer_id": "C0084",
        "transaction_date": "2026-01-28",
        "transaction_time": "18:19",
        "merchant": "Online Marketplace",
        "transaction_amount": 845.75,
        "location": "Charlotte NC",
        "payment_method": "Debit Card",
        "account_age_days": 260,
        "fraud_flag": 1
    },

    # Scenario 4: Repeated round-dollar transactions
    {
        "transaction_id": "T010010",
        "customer_id": "C0091",
        "transaction_date": "2026-03-02",
        "transaction_time": "11:05",
        "merchant": "Wire Transfer",
        "transaction_amount": 2000.00,
        "location": "Savannah GA",
        "payment_method": "Credit Card",
        "account_age_days": 710,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010011",
        "customer_id": "C0091",
        "transaction_date": "2026-03-02",
        "transaction_time": "11:17",
        "merchant": "Wire Transfer",
        "transaction_amount": 2000.00,
        "location": "Savannah GA",
        "payment_method": "Credit Card",
        "account_age_days": 710,
        "fraud_flag": 1
    },
    {
        "transaction_id": "T010012",
        "customer_id": "C0091",
        "transaction_date": "2026-03-02",
        "transaction_time": "11:29",
        "merchant": "Wire Transfer",
        "transaction_amount": 2000.00,
        "location": "Savannah GA",
        "payment_method": "Credit Card",
        "account_age_days": 710,
        "fraud_flag": 1
    },

    # Scenario 5: Legitimate but unusual transaction
    {
        "transaction_id": "T010013",
        "customer_id": "C0042",
        "transaction_date": "2026-02-10",
        "transaction_time": "01:45",
        "merchant": "Hotel",
        "transaction_amount": 3200.00,
        "location": "Miami FL",
        "payment_method": "Credit Card",
        "account_age_days": 1450,
        "fraud_flag": 0
    }
]

transactions.extend(suspicious_transactions)
df = pd.DataFrame(transactions)

df.to_csv("data/transactions.csv", index=False)

print(f"Created {len(df)} transactions.")
print(df.head())