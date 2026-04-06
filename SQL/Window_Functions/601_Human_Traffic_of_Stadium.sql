-- https://leetcode.com/problems/human-traffic-of-stadium/
-- Сложность: Hard
-- Тема: CTE / Window Functions / Gaps & Islands

-- Шаг 1: Отфильтровываем нужные дни и находим "идентификаторы островов"
WITH People AS(
    SELECT
        id,
        visit_date,
        people,
        -- Магия Gaps & Islands: вычитаем порядковый номер из реального ID.
        -- Для строк, идущих подряд, эта разница будет одинаковой!
        id - ROW_NUMBER() OVER (ORDER BY id) AS island_id
    FROM Stadium
    WHERE people >= 100
),

-- Шаг 2: Считаем размер каждого "острова"
Days AS(
    SELECT
        id,
        visit_date,
        people,
        -- Считаем количество дней в каждом острове
        COUNT(*) OVER(PARTITION BY island_id) AS sum_day
    FROM People
)

-- Шаг 3: Оставляем только те острова, где 3 и более дней подряд
SELECT
    id,
    visit_date,
    people
FROM Days
WHERE sum_day >= 3
ORDER BY visit_date;