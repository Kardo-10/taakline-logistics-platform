SELECT
    primary_item,
    ROUND(SUM(total_amount),2) AS revenue
FROM orders
WHERE primary_item NOT LIKE 'Order-%'
GROUP BY primary_item
ORDER BY revenue DESC
LIMIT 10;