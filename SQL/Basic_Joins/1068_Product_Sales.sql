-- https://leetcode.com/problems/product-sales-analysis-i/
-- Сложность: Easy
-- Тема: Basic Joins (INNER JOIN)

SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales AS s
-- Объединяем продажи с описанием продуктов по product_id
JOIN Product AS p ON s.product_id = p.product_id;