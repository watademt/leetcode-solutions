-- https://leetcode.com/problems/game-play-analysis-iv/
-- Сложность: Medium
-- Тема: LEFT JOIN / CTE / Aggregation

WITH First_date AS (
    SELECT player_id, MIN(event_date) AS min_date
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(a.player_id) / COUNT(f.player_id), 2) AS fraction
FROM First_date AS f
LEFT JOIN Activity AS a
    ON a.player_id = f.player_id
    AND a.event_date = DATE_ADD(f.min_date, INTERVAL 1 DAY);