-- https://leetcode.com/problems/immediate-food-delivery-ii/
-- Сложность: Medium
-- Тема: CTE / LEFT JOIN / Aggregation / Fractions

WITH Immediate AS (
    SELECT customer_id, MIN(order_date) AS min_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT
    ROUND(COUNT(d.customer_id) / COUNT(i.customer_id) * 100, 2) AS immediate_percentage
FROM Immediate AS i
LEFT JOIN Delivery AS d
    ON d.customer_id = i.customer_id
    AND d.customer_pref_delivery_date = i.min_date;