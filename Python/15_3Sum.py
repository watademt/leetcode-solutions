# https://leetcode.com/problems/3sum/
# Сложность: Medium
# Тема: Array / Two Pointers / Sorting

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Сортируем массив, чтобы использовать два указателя и легко избегать дубликатов
        nums.sort()
        result = []

        # Фиксируем первый элемент тройки
        for i in range(len(nums)):
            # Если текущий элемент такой же, как предыдущий, пропускаем его (избегаем дубликатов троек)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Ставим указатели на оставшуюся часть массива
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Нашли нужную сумму
                if nums[left] + nums[right] == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])

                    # Сдвигаем оба указателя
                    left += 1
                    right -= 1

                    # Пропускаем дубликаты для левого указателя
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                # Если сумма слишком большая, уменьшаем правый указатель
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1

                # Если сумма слишком маленькая, увеличиваем левый указатель
                else:
                    left += 1

        return result