-- https://leetcode.com/problems/patients-with-a-condition/
-- Сложность: Easy
-- Тема: String Functions / Pattern Matching (LIKE)

SELECT * FROM Patients
-- Ищем DIAB1 либо в начале строки, либо после пробела
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';