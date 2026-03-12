# https://leetcode.com/problems/surrounded-regions/
# Сложность: Medium
# Тема: Array / Depth-First Search / Breadth-First Search / Matrix

class Solution(object):
    def change(self, board, row, col):
        rows = len(board)
        cols = len(board[0])

        # Условие выхода: за границами или клетка НЕ является 'O'
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
            return

        # Временно помечаем как спасенную
        board[row][col] = 'S'

        # Рекурсивно спасаем соседей
        self.change(board, row + 1, col)
        self.change(board, row - 1, col)
        self.change(board, row, col + 1)
        self.change(board, row, col - 1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        # 1. Проверяем верхнюю границу
        for j in range(cols):
            if board[0][j] == 'O':
                self.change(board, 0, j)

        # 2. Проверяем правую границу
        for i in range(1, rows):
            if board[i][cols - 1] == 'O':
                self.change(board, i, cols - 1)

        # 3. Проверяем нижнюю границу
        if rows > 1:
            for j in range(cols - 2, -1, -1):
                if board[rows - 1][j] == 'O':
                    self.change(board, rows - 1, j)

        # 4. Проверяем левую границу
        if cols > 1:
            for i in range(rows - 2, 0, -1):
                if board[i][0] == 'O':
                    self.change(board, i, 0)

        # 5. Финальная зачистка и восстановление
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        return board