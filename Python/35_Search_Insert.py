# https://leetcode.com/problems/search-insert-position/
# Сложность: Easy
# Тема: Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Если число не найдено, left укажет на позицию для вставки
        return left


# --- Примеры для проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Пример 1: {sol.searchInsert([1, 3, 5, 6], 5)}")  # Вывод: 2
    print(f"Пример 2: {sol.searchInsert([1, 3, 5, 6], 2)}")  # Вывод: 1
    print(f"Пример 3: {sol.searchInsert([1, 3, 5, 6], 7)}")  # Вывод: 4