# https://leetcode.com/problems/container-with-most-water/
# Сложность: Medium
# Тема: Array / Two Pointers / Greedy

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Ставим указатели на начало и конец массива
        p1 = 0
        p2 = len(height) - 1
        max_area = 0

        # Сдвигаем указатели навстречу друг другу
        while p1 < p2:
            # Считаем текущую площадь: ширина * минимальную высоту стенки
            max_area = max(max_area, (p2 - p1) * min(height[p1], height[p2]))

            # Жертвуем шириной, сдвигая указатель с меньшей высотой в поисках большей
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return max_area