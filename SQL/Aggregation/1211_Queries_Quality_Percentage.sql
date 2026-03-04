-- https://leetcode.com/problems/queries-quality-and-percentage/
-- Сложность: Easy
-- Тема: Group By / Conditional Aggregation / AVG

SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;