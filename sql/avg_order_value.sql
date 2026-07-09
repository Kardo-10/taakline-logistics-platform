SELECT
    order_month,
    order_year,
    ROUND(AVG(total_amount),2) AS avg_order_value
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, avg_order_value DESC;
