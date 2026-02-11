# https://leetcode.com/problems/majority-element/
# Сложность: Easy
# Тема: Array / Boyer-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Алгоритм Бойера-Мура (Голосование)
        candidate = nums[0]
        count = 1

        # Начинаем со второго элемента
        for num in nums[1:]:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate