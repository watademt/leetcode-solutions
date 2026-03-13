# https://leetcode.com/problems/house-robber-ii/
# Сложность: Medium
# Тема: Array / Dynamic Programming

class Solution(object):
    def helper(self, nums):
        prev1 = 0
        prev2 = 0

        for current_house in nums:
            current_max = max(prev2 + current_house, prev1)
            prev2 = prev1
            prev1 = current_max

        return prev1

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Если дом всего один, грабим его и уходим
        if len(nums) == 1:
            return nums[0]

        # Выбираем максимум из двух сценариев:
        # 1. Без последнего дома
        # 2. Без первого дома
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))