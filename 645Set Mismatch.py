# https://leetcode.com/problems/set-mismatch/
# Сложность: Easy
# Тема: Math / Set

class Solution(object):
    def findErrorNums(self, nums):
        """
        Находит дублирующееся и пропущенное число в наборе от 1 до n.
        Использует математический подход через разность сумм.
        """
        n = len(nums)
        # Находим дубликат: (сумма всех чисел) - (сумма уникальных чисел)
        duplicate = sum(nums) - sum(set(nums))

        # Находим пропущенное: (идеальная сумма 1..n) - (сумма уникальных чисел)
        missing = sum(range(1, n + 1)) - sum(set(nums))

        return [duplicate, missing]


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 [1,2,2,4]: {sol.findErrorNums([1, 2, 2, 4])}")  # Ожидаемый вывод: [2, 3]
    print(f"Тест 2 [1,1]: {sol.findErrorNums([1, 1])}")  # Ожидаемый вывод: [1, 2]