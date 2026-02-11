-- https://leetcode.com/problems/classes-more-than-5-students/
-- Сложность: Easy
-- Тема: Group By / Having

SELECT class
FROM Courses
GROUP BY class
-- Фильтруем уже сгруппированные данные: в классе должно быть >= 5 студентов
HAVING COUNT(student) >= 5;