# https://leetcode.com/problems/single-number/
# Сложность: Easy
# Тема: Bit Manipulation (XOR)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0
        for num in nums:
            # XOR (^) работает так:
            # a ^ 0 = a
            # a ^ a = 0
            # Поэтому все пары "уничтожат" друг друга, останется уникальное число.
            unique ^= num
        return unique