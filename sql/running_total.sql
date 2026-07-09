SELECT
    completed_date,
    total_amount,
    SUM(total_amount) OVER (
        ORDER BY completed_date
    ) AS running_total
FROM orders
ORDER BY completed_date;