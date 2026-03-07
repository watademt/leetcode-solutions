# https://leetcode.com/problems/binary-tree-right-side-view/
# Сложность: Medium
# Тема: Tree / Breadth-First Search / Queue

from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Добавляем в результат только последний элемент на текущем уровне
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result