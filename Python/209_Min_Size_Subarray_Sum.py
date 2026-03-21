# https://leetcode.com/problems/minimum-size-subarray-sum/
# Сложность: Medium
# Тема: Array / Binary Search / Sliding Window / Prefix Sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_sum = 0
        # Инициализируем минимальную длину бесконечностью
        min_len = float('inf')

        for right in range(len(nums)):
            # Расширяем окно: добавляем элемент в текущую сумму
            current_sum += nums[right]

            # Пока условие выполняется, пытаемся сузить окно слева,
            # чтобы найти минимально возможную длину
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)

                # Убираем самый левый элемент из суммы и сдвигаем левый указатель
                current_sum -= nums[left]
                left += 1

        # Если min_len так и остался бесконечностью, возвращаем 0 (подмассив не найден)
        return min_len if min_len != float('inf') else 0