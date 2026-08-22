-- Investigation 1:
-- Identify transactions classified as high risk

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


-- Investigation 2:
-- Identify customers with the greatest high-risk financial exposure

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


-- Investigation 3:
-- Summarize risk levels across the entire dataset

SELECT
    risk_level,
    COUNT(*) AS transaction_count,
    SUM(transaction_amount) AS total_transaction_value,
    AVG(risk_score) AS average_risk_score
FROM transactions
GROUP BY risk_level
ORDER BY average_risk_score DESC;


-- Investigation 4:
-- Identify merchants associated with the highest-risk activity

SELECT
    merchant,
    COUNT(*) AS flagged_transactions,
    SUM(transaction_amount) AS total_flagged_amount,
    AVG(risk_score) AS average_risk_score
FROM transactions
WHERE risk_level IN ('Medium', 'High')
GROUP BY merchant
ORDER BY total_flagged_amount DESC;


-- Investigation 5:
-- Identify customers with multiple Medium or High risk transactions

SELECT
    customer_id,
    COUNT(*) AS flagged_transactions,
    SUM(transaction_amount) AS total_flagged_amount,
    MAX(risk_score) AS maximum_risk_score
FROM transactions
WHERE risk_level IN ('Medium', 'High')
GROUP BY customer_id
HAVING COUNT(*) >= 2
ORDER BY total_flagged_amount DESC;