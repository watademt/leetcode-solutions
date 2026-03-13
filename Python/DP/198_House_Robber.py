# https://leetcode.com/problems/house-robber/
# Сложность: Medium
# Тема: Array / Dynamic Programming

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Инициализируем переменные для хранения двух предыдущих состояний
        prev1 = 0
        prev2 = 0

        # Главная логика DP сама справляется с массивами любой длины
        for current_house in nums:
            # Выбираем максимум: грабим этот дом + пред-предыдущий, ИЛИ пропускаем и берем предыдущий
            current_max = max(prev2 + current_house, prev1)

            # Сдвигаем "окно" памяти на один шаг вперед
            prev2 = prev1
            prev1 = current_max

        return prev1