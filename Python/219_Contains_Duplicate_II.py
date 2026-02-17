# https://leetcode.com/problems/contains-duplicate-ii/
# Сложность: Easy
# Тема: Hash Table / Sliding Window

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Словарь: {число: последний_индекс}
        seen = {}

        for i, num in enumerate(nums):
            # Если число уже видели и оно близко
            if num in seen and abs(i - seen[num]) <= k:
                return True

            # Запоминаем новый (самый свежий) индекс числа
            seen[num] = i

        return False