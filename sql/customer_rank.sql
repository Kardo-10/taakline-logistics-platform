SELECT
    customer_name,
    ROUND(SUM(total_amount),2) AS revenue,
    RANK() OVER (
        ORDER BY SUM(total_amount) DESC
    ) AS customer_rank
FROM orders
GROUP BY customer_name;
