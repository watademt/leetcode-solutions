-- https://leetcode.com/problems/find-customer-referee/
-- Сложность: Easy
-- Тема: Select / Handling NULL values

SELECT name
FROM Customer
-- NULL не равен ничему, поэтому используем явную проверку IS NULL
WHERE referee_id != 2 OR referee_id IS NULL;