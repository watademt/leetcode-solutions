class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        result = [sum(nums) - sum(set(nums))]
        result. append(sum(range(1, n+1)) - sum(set(nums)))
        return result