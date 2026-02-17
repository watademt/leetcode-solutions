-- https://leetcode.com/problems/exchange-seats/
-- Сложность: Medium
-- Тема: Control Flow / Math Logic

SELECT
    CASE
        -- Если ID четный -> уменьшаем на 1 (меняем с предыдущим)
        WHEN MOD(id, 2) = 0 THEN id - 1
        -- Если ID нечетный И он последний -> оставляем как есть
        WHEN id = (SELECT COUNT(*) FROM Seat) THEN id
        -- Если ID нечетный (и не последний) -> увеличиваем на 1 (меняем со следующим)
        ELSE id + 1
    END AS id,
    student
FROM Seat
ORDER BY id;