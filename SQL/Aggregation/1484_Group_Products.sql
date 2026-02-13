-- https://leetcode.com/problems/group-sold-products-by-the-date/
-- Сложность: Easy
-- Тема: Aggregation / String Manipulation (GROUP_CONCAT)

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    -- Склеиваем уникальные продукты через запятую, сортируя их по алфавиту
    GROUP_CONCAT(
        DISTINCT product
        ORDER BY product
        SEPARATOR ','
    ) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;