-- https://leetcode.com/problems/employees-whose-manager-left-the-company/
-- Сложность: Easy
-- Тема: Subqueries / Filtering

SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  -- Ищем тех, чей менеджер НЕ в списке сотрудников
  AND manager_id NOT IN (
      SELECT employee_id FROM Employees
  )
ORDER BY employee_id;