-- https://leetcode.com/problems/tree-node/
-- Сложность: Medium
-- Тема: Control Flow / CASE WHEN / Subqueries

SELECT
    id,
    CASE
        -- Если нет родителя, то это корень дерева
        WHEN p_id IS NULL THEN 'Root'
        -- Если этот id встречается в списке родителей (p_id), значит у него есть дети
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        -- Все остальные узлы (без детей) — это листья
        ELSE 'Leaf'
    END AS type
FROM Tree;