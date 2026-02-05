# https://leetcode.com/problems/matrix-diagonal-sum/
# Сложность: Easy
# Тема: Matrix / Array

class Solution(object):
    def diagonalSum(self, mat):
        """
        Вычисляет сумму элементов главной и побочной диагоналей квадратной матрицы.
        Элементы, принадлежащие обеим диагоналям, учитываются один раз.
        """
        n = len(mat)
        sum_d = 0

        for i in range(n):
            # Суммируем элементы главной диагонали (i, i)
            sum_d += mat[i][i]
            # Суммируем элементы побочной диагонали (i, n - 1 - i)
            sum_d += mat[i][n - 1 - i]

        # Если размер матрицы нечетный, вычитаем центральный элемент,
        # так как он был добавлен дважды.
        if n % 2 == 1:
            center_index = n // 2
            sum_d -= mat[center_index][center_index]

        return sum_d


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()

    # Тест 1: Нечетная матрица 3x3
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(f"Тест 1 (3x3): {sol.diagonalSum(mat1)}")  # Ожидаемый вывод: 25 (1+5+9 + 3+7 - 5)

    # Тест 2: Четная матрица 2x2
    mat2 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    print(f"Тест 2 (4x4): {sol.diagonalSum(mat2)}")  # Ожидаемый вывод: 8