-- https://leetcode.com/problems/confirmation-rate/
-- Сложность: Medium
-- Тема: LEFT JOIN / Conditional Aggregation / AVG

SELECT
    s.user_id,
    ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY user_id;