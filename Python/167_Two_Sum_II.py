# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Сложность: Medium
# Тема: Array / Two Pointers / Binary Search

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                # По условию задачи индексы начинаются с 1
                return [left + 1, right + 1]