-- https://leetcode.com/problems/employees-earning-more-than-managers/
-- Сложность: Easy
-- Тема: Self Join

SELECT
    e.name AS Employee
FROM Employee AS e
-- Соединяем таблицу саму с собой:
-- e - работник, m - его менеджер
JOIN Employee AS m ON e.managerId = m.id
WHERE e.salary > m.salary;