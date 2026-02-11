-- https://leetcode.com/problems/game-play-analysis-i/
-- Сложность: Easy
-- Тема: Aggregation (MIN) / Group By

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;