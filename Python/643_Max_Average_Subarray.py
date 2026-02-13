# https://leetcode.com/problems/maximum-average-subarray-i/
# Сложность: Easy
# Тема: Sliding Window

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 1. Считаем сумму первого окна
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        # 2. Скользим окном
        for i in range(k, len(nums)):
            # Прибавляем новый элемент (справа), вычитаем старый (слева)
            curr_sum += nums[i] - nums[i - k]

            if curr_sum > max_sum:
                max_sum = curr_sum

        # Важно: преобразуем во float для точного деления
        return float(max_sum) / k