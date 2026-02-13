-- https://leetcode.com/problems/rank-scores/
-- Сложность: Medium
-- Тема: Window Functions (DENSE_RANK)

SELECT
    score,
    -- DENSE_RANK создает рейтинг без дырок (1, 1, 2, 3...)
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;