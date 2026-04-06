# https://leetcode.com/problems/product-of-array-except-self/
# Сложность: Medium
# Тема: Array / Prefix Sum

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        left_mult = 1
        right_mult = 1

        # 1. Проход слева направо:
        # Кладем в answer[i] произведение всех элементов СЛЕВА от nums[i]
        for i in range(n):
            answer[i] = left_mult
            left_mult *= nums[i]

        # 2. Проход справа налево:
        # Домножаем текущий answer[i] на произведение всех элементов СПРАВА от nums[i]
        for i in range(n - 1, -1, -1):
            answer[i] *= right_mult
            right_mult *= nums[i]

        return answer