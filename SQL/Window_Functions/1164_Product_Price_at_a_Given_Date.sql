-- https://leetcode.com/problems/product-price-at-a-given-date/
-- Сложность: Medium
-- Тема: Database / Window Function / UNION

-- Шаг 1: Находим все изменения цен до или в день 2019-08-16
WITH Products_Date AS(
    SELECT
        product_id,
        new_price,
        change_date,
        -- Нумеруем изменения по убыванию даты для каждого продукта
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS num
    FROM Products
    WHERE change_date <= "2019-08-16"
)
-- Забираем самую свежую цену на указанную дату (где num = 1)
SELECT
    product_id,
    new_price AS price
FROM Products_Date
WHERE num = 1

UNION

-- Шаг 2: Находим продукты, у которых ВСЕ изменения были строго после 2019-08-16
SELECT
    product_id,
    10 AS price -- Устанавливаем дефолтную цену
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';