class Solution(object):
    def shuffle(self, nums, n):
        nums1 = nums[:n]
        nums2 = nums[n:]
        result = []
        for a, b in zip(nums1, nums2):
            result.append(a)
            result.append(b)
        return (result)
