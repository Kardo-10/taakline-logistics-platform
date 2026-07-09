SELECT
    order_month,
    order_year,
    ROUND(SUM(total_amount),2) AS revenue
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, revenue DESC;