# https://leetcode.com/problems/perfect-squares/
# Сложность: Medium
# Тема: Math / Dynamic Programming / Breadth-First Search

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Оптимизация: если число уже является идеальным квадратом, нужна всего 1 "монета"
        if int(n ** 0.5) ** 2 == n:
            return 1

        # Создаем кэш (шпаргалку) и заполняем "бесконечностью"
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Идем по всем числам от 1 до n
        for i in range(1, n + 1):
            j = 1
            # Генерируем "квадратные монеты", пока они помещаются в текущее число i
            while j * j <= i:
                coin = j * j
                # Выбираем минимум: либо текущее значение, либо 1 монета + остаток из кэша
                dp[i] = min(dp[i], dp[i - coin] + 1)
                j += 1

        # По условию задачи мы всегда найдем ответ (т.к. есть монета 1),
        # но для страховки оставляем ту же структуру возврата, что и в Coin Change
        if dp[n] == float('inf'):
            return -1
        else:
            return dp[n]