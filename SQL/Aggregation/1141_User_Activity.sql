-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Сложность: Easy
-- Тема: GROUP BY / DATE manipulation

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date <= '2019-07-27'
  AND activity_date > '2019-07-27' - INTERVAL 30 DAY
GROUP BY activity_date;