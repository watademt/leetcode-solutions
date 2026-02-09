-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Сложность: Easy
-- Тема: Basic Select

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';