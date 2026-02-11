-- https://leetcode.com/problems/rising-temperature/
-- Сложность: Easy
-- Тема: Self Join / Date Functions

SELECT w1.id
FROM Weather AS w1
-- Соединяем таблицу саму с собой, чтобы сравнить "сегодня" (w1) и "вчера" (w2)
JOIN Weather AS w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;