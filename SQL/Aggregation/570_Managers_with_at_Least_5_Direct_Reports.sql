-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Сложность: Medium
-- Тема: CTE / GROUP BY / HAVING / JOIN

WITH ManagerReports AS (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
SELECT e.name
FROM Employee e
JOIN ManagerReports mr ON e.id = mr.managerId;