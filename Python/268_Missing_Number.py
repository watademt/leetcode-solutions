# https://leetcode.com/problems/missing-number/
# Сложность: Easy
# Тема: Math / Array

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Сумма арифметической прогрессии от 0 до n
        # минус сумма реальных чисел = пропущенное число.
        n = len(nums)
        expected_sum = sum(range(n + 1))
        actual_sum = sum(nums)

        return expected_sum - actual_sum