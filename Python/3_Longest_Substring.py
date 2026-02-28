# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Сложность: Medium
# Тема: Sliding Window / Hash Table / String

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in my_dict and my_dict[char] >= left:
                left = my_dict[char] + 1

            my_dict[char] = right
            if (right - left + 1) > max_len:
                max_len = right - left + 1

        return max_len