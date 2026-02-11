# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Сложность: Easy
# Тема: Array / Dynamic Programming / Greedy

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Инициализируем минимум первой ценой
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Если нашли цену ниже текущего минимума — обновляем минимум
            if price < min_price:
                min_price = price
            # Иначе проверяем, не максимальная ли это прибыль на сегодня
            elif (price - min_price) > max_profit:
                max_profit = price - min_price

        return max_profit