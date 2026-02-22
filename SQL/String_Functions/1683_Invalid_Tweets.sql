-- https://leetcode.com/problems/invalid-tweets/
-- Сложность: Easy
-- Тема: String Functions / Filtering

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;