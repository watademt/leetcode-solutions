-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Сложность: Medium
-- Тема: CTE / UNION ALL / Aggregation / ORDER BY

-- Шаг 1: Собираем всех друзей (и тех, кто отправил заявку, и тех, кто принял)
-- в одну длинную вертикальную колонку 'id'.
-- Используем UNION ALL, чтобы сохранить все дубликаты (каждый дубликат = 1 друг).
WITH Sum_Friends AS (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
)

-- Шаг 2: Считаем, сколько раз встречается каждый id, сортируем по убыванию
-- и забираем только первого победителя.
SELECT
    id,
    COUNT(*) AS num
FROM Sum_Friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;