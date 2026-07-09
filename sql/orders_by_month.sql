SELECT
    order_month,
    order_year,
    COUNT(*) AS orders
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, orders DESC;