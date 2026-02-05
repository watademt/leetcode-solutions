# https://leetcode.com/problems/two-sum/
# Задача: Найти индексы двух чисел, сумма которых равна target.

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# --- Примеры для проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Ожидаемый вывод: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # Ожидаемый вывод: [1, 2]