# https://leetcode.com/problems/max-area-of-island/
# Сложность: Medium
# Тема: Array / Depth-First Search / Matrix

class Solution(object):
    def island(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        # Выход за границы или наткнулись на воду (проверяем число 0)
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0

            # "Топим" сушу, чтобы не зациклить рекурсию
        grid[row][col] = 0

        # Считаем площадь: 1 (эта клетка) + площадь всех соседей
        area = 1
        area += self.island(grid, row + 1, col)
        area += self.island(grid, row - 1, col)
        area += self.island(grid, row, col + 1)
        area += self.island(grid, row, col - 1)

        return area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Ищем сушу (проверяем число 1)
                if grid[i][j] == 1:
                    # Запускаем DFS и обновляем максимальную площадь
                    current_size = self.island(grid, i, j)
                    max_size = max(max_size, current_size)

        return max_size