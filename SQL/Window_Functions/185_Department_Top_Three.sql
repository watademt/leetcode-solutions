-- https://leetcode.com/problems/department-top-three-salaries/
-- Сложность: Hard
-- Тема: Window Functions / CTE / Joins

WITH Department_n AS(
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY e.salary DESC
        ) AS rang
    FROM Department d
    JOIN Employee e ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM Department_n
WHERE rang <= 3
ORDER BY Salary;