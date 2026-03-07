# https://leetcode.com/problems/symmetric-tree/
# Сложность: Easy
# Тема: Tree / Depth-First Search / Recursion

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        else:
            if p.val == q.val:
                # Зеркальное сравнение: левый-правый и правый-левый
                return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
            else:
                return False