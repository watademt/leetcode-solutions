# https://leetcode.com/problems/trapping-rain-water/
# Сложность: Hard
# Тема: Array / Two Pointers

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        water = 0

        while left < right:
            # Двигаем тот указатель, чья максимальная "стена" ниже
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]

        return water