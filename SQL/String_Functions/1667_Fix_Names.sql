-- https://leetcode.com/problems/fix-names-in-a-table/
-- Сложность: Easy
-- Тема: String Manipulation (UPPER, LOWER, SUBSTRING)

SELECT
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)), -- Первая буква заглавная
        LOWER(SUBSTRING(name, 2))     -- Остальные строчные
    ) AS name
FROM Users
ORDER BY user_id;