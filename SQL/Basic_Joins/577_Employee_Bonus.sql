-- https://leetcode.com/problems/employee-bonus/
-- Сложность: Easy
-- Тема: LEFT JOIN / NULL Handling

SELECT
    e.name,
    b.bonus
FROM Employee AS e
-- Используем LEFT JOIN, чтобы не потерять сотрудников без бонусов
LEFT JOIN Bonus AS b ON e.empId = b.empId
-- Важно: NULL не участвует в сравнении < 1000, его нужно проверять отдельно
WHERE b.bonus < 1000 OR b.bonus IS NULL;