# https://leetcode.com/problems/binary-search/
# Сложность: Easy
# Тема: Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        Классический бинарный поиск в отсортированном массиве.
        Возвращает индекс цели или -1, если цель не найдена.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Цель в правой половине
                left = mid + 1
            else:
                # Цель в левой половине
                right = mid - 1

        return -1


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 (найти 9): {sol.search([-1, 0, 3, 5, 9, 12], 9)}")  # Ожидаемый вывод: 4
    print(f"Тест 2 (найти 2): {sol.search([-1, 0, 3, 5, 9, 12], 2)}")  # Ожидаемый вывод: -1