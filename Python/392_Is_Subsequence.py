# https://leetcode.com/problems/is-subsequence/
# Сложность: Easy
# Тема: Two Pointers / String

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index_s = 0
        index_t = 0

        while (index_s < len(s)) and (index_t < len(t)):
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_t += 1

        if index_s == len(s):
            return True
        else:
            return False