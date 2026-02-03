class Solution(object):
    def moveZeroes(self, nums):
        write_index = 0
        for num in nums:
            if num != 0:
                nums[write_index] = num
                write_index += 1
        nums[write_index:] = [0]*(len(nums) - write_index)
        return nums