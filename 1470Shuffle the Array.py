# https://leetcode.com/problems/shuffle-the-array/
# Сложность: Easy
# Тема: Array / Simulation

class Solution(object):
    def shuffle(self, nums, n):
        """
        Перетасовывает массив в формате [x1, y1, x2, y2, ..., xn, yn].
        """
        # Делим массив на две части
        nums1 = nums[:n]
        nums2 = nums[n:]

        result = []
        # Объединяем элементы парами
        for a, b in zip(nums1, nums2):
            result.append(a)
            result.append(b)

        return result


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 [2,5,1,3,4,7]: {sol.shuffle([2, 5, 1, 3, 4, 7], 3)}")
    # Ожидаемый вывод: [2, 3, 5, 4, 1, 7]

    print(f"Тест 2 [1,2,3,4,4,3,2,1]: {sol.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)}")
    # Ожидаемый вывод: [1, 4, 2, 3, 3, 2, 4, 1]