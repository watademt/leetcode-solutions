-- https://leetcode.com/problems/restaurant-growth/
-- Сложность: Medium
-- Тема: Window Functions / ROWS BETWEEN / CTE

WITH Revenue AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
), Revenue1 AS (
    SELECT
        visited_on,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM Revenue
)
SELECT
    visited_on,
    amount,
    average_amount
FROM Revenue1
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6;