# https://leetcode.com/problems/max-consecutive-ones/
# Сложность: Easy
# Тема: Array / Simple Iteration

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Находит максимальное количество идущих подряд единиц в массиве.
        """
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                # Если встретили 0, сбрасываем текущий счетчик
                count = 0

            # На каждом шаге проверяем, не стал ли текущий счетчик больше максимального
            if count > max_count:
                max_count = count

        return max_count


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 [1,1,0,1,1,1]: {sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])}")  # Ожидаемый вывод: 3
    print(f"Тест 2 [1,0,1,1,0,1]: {sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])}")  # Ожидаемый вывод: 2