class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        if sum (nums) == sum(set(nums)):
            result = False
        else:
            result = True
        return result