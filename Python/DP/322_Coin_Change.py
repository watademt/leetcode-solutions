# https://leetcode.com/problems/coin-change/
# Сложность: Medium
# Тема: Array / Dynamic Programming / Breadth-First Search

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Создаем массив dp, заполненный "бесконечностью". Размер amount + 1.
        dp = [float('inf')] * (amount + 1)

        # Базовый случай: чтобы собрать сумму 0, нужно 0 монет
        dp[0] = 0

        # Идем по всем суммам от 1 до amount
        for current_amount in range(1, amount + 1):
            # Пробуем применить каждую монету
            for coin in coins:
                if coin <= current_amount:
                    # Выбираем минимум: либо то, что уже было,
                    # либо 1 текущая монета + минимальное кол-во монет для оставшейся суммы
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

        # Если в конце так и осталась бесконечность, значит сумму не собрать
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]