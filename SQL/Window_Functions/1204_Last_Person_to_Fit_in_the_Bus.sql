-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/
-- Сложность: Medium
-- Тема: Window Functions / CTE / Running Total

WITH Total_weight AS (
    SELECT
        person_name,
        turn,
        -- Считаем нарастающий итог веса пассажиров в порядке очереди
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
-- Фильтруем тех, кто влез в лимит, сортируем очередь в обратном порядке и берем первого (т.е. последнего зашедшего)
SELECT person_name
FROM Total_weight
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;