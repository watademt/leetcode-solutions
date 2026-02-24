-- https://leetcode.com/problems/product-sales-analysis-iii/
-- Сложность: Medium
-- Тема: CTE (WITH) / Joins

WITH FirstSales AS(
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)
SELECT s.product_id, f.first_year AS first_year, s.quantity, s.price
FROM Sales AS s
JOIN FirstSales AS f
    ON s.product_id = f.product_id
    AND s.year = f.first_year;