# https://leetcode.com/problems/move-zeroes/
# Сложность: Easy
# Тема: Two Pointers / Array Transformation

class Solution(object):
    def moveZeroes(self, nums):
        """
        Перемещает все нули в конец массива, сохраняя относительный порядок
        ненулевых элементов. Модифицирует массив на месте.
        """
        write_index = 0

        for num in nums:
            if num != 0:
                nums[write_index] = num
                write_index += 1

        nums[write_index:] = [0] * (len(nums) - write_index)

        return nums


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    test_1 = [0, 1, 0, 3, 12]
    print(f"Тест 1: {sol.moveZeroes(test_1)}")  # Ожидаемый вывод: [1, 3, 12, 0, 0]

    test_2 = [0]
    print(f"Тест 2: {sol.moveZeroes(test_2)}")  # Ожидаемый вывод: [0]