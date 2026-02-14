# https://leetcode.com/problems/intersection-of-two-arrays/
# Сложность: Easy
# Тема: Set / Array / Hash Set

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Превращаем списки в множества для поиска пересечения за O(1)
        # set1 & set2 возвращает только общие элементы
        return list(set(nums1) & set(nums2))