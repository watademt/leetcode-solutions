# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Сложность: Easy
# Тема: Tree / Depth-First Search / Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1