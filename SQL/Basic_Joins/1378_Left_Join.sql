-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Сложность: Easy
-- Тема: Basic Joins (LEFT JOIN)

SELECT
    eUNI.unique_id,
    e.name
FROM Employees AS e
-- Используем LEFT JOIN, чтобы не потерять сотрудников без unique_id
LEFT JOIN EmployeeUNI AS eUNI ON e.id = eUNI.id;