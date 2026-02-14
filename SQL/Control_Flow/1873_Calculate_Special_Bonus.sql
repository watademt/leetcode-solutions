-- https://leetcode.com/problems/calculate-special-bonus/
-- Сложность: Easy
-- Тема: Control Flow (CASE WHEN)

SELECT
    employee_id,
    CASE
        -- Нечетный ID и имя не начинается на 'M'
        WHEN employee_id % 2 != 0 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;