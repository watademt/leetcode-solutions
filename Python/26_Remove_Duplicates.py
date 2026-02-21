# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Сложность: Easy
# Тема: Array / Two Pointers

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write