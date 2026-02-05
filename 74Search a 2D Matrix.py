# https://leetcode.com/problems/search-a-2d-matrix/
# Сложность: Medium
# Описание: Поиск числа в отсортированной матрице с использованием бинарного поиска.

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1  # Важно: индекс последнего элемента (N-1)

        while left <= right:
            idx = (left + right) // 2
            # Перевод виртуального индекса в координаты матрицы
            current_element = matrix[idx // cols][idx % cols]

            if current_element == target:
                return True
            elif current_element < target:
                left = idx + 1
            else:
                right = idx - 1
        return False


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    test_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

    print(f"Поиск 3: {sol.searchMatrix(test_matrix, 3)}")  # Ожидаемый результат: True
    print(f"Поиск 13: {sol.searchMatrix(test_matrix, 13)}")  # Ожидаемый результат: False