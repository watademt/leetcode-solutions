# https://leetcode.com/problems/merge-sorted-array/
# Сложность: Easy
# Тема: Two Pointers (С конца)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Указатели на концы значимых частей массивов
        p1 = m - 1
        p2 = n - 1
        # Указатель на самый конец массива nums1
        p = m + n - 1

        # Пока во втором массиве еще есть числа
        while p2 >= 0:
            # Если в первом массиве еще есть числа и число в nums1 больше
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Если число в nums2 больше или nums1 уже закончился
                nums1[p] = nums2[p2]
                p2 -= 1

            # Сдвигаем общий указатель записи влево
            p -= 1

        return nums1


# --- Примеры для проверки ---
if __name__ == "__main__":
    sol = Solution()

    # Тест 1
    n1 = [1, 2, 3, 0, 0, 0]
    n2 = [2, 5, 6]
    print(f"Результат слияния: {sol.merge(n1, 3, n2, 3)}")
    # Ожидаемый вывод: [1, 2, 2, 3, 5, 6]

    # Тест 2 (когда nums1 пустой)
    n3 = [0]
    n4 = [1]
    print(f"Результат слияния (пустой nums1): {sol.merge(n3, 0, n4, 1)}")
    # Ожидаемый вывод: [1]