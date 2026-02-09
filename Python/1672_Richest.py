# https://leetcode.com/problems/richest-customer-wealth/
# Сложность: Easy
# Тема: Array / Matrix / Simulation

class Solution(object):
    def maximumWealth(self, accounts):
        """
        Находит богатство самого состоятельного клиента.
        Богатство клиента — это сумма денег на всех его банковских счетах.
        """
        # Считаем сумму для каждой строки (клиента)
        row_sums = [sum(row) for row in accounts]
        # Возвращаем максимальное значение из полученного списка сумм
        return max(row_sums)


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()

    # Тест 1
    accounts1 = [[1, 2, 3], [3, 2, 1]]
    print(f"Тест 1: {sol.maximumWealth(accounts1)}")  # Ожидаемый вывод: 6

    # Тест 2
    accounts2 = [[1, 5], [7, 3], [3, 5]]
    print(f"Тест 2: {sol.maximumWealth(accounts2)}")  # Ожидаемый вывод: 10

    # Тест 3
    accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(f"Тест 3: {sol.maximumWealth(accounts3)}")  # Ожидаемый вывод: 17