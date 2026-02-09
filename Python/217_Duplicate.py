# https://leetcode.com/problems/contains-duplicate/
# Сложность: Easy
# Тема: Hash Set

class Solution(object):
    def containsDuplicate(self, nums):
        # Если длина списка не совпадает с длиной множества (set),
        # значит в списке были повторяющиеся элементы.
        return len(nums) != len(set(nums))

# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 [1,2,3,1]: {sol.containsDuplicate([1,2,3,1])}") # True
    print(f"Тест 2 [1,2,3,4]: {sol.containsDuplicate([1,2,3,4])}") # False