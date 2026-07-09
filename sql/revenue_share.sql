SELECT
    customer_name,
    ROUND(SUM(total_amount),2) AS revenue,
    ROUND(
        SUM(total_amount) * 100.0
        / SUM(SUM(total_amount)) OVER (),
        2
    ) AS revenue_percent
FROM orders
GROUP BY customer_name
ORDER BY revenue DESC;
