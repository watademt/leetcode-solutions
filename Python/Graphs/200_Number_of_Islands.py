# https://leetcode.com/problems/number-of-islands/
# Сложность: Medium
# Тема: Array / Depth-First Search / Breadth-First Search / Matrix

class Solution(object):
    def flooding(self, grid, r, e):
        rows = len(grid)
        cols = len(grid[0])

        # Проверка выхода за границы или попадания в воду
        if r < 0 or r >= rows or e < 0 or e >= cols or grid[r][e] == '0':
            return

        # "Топим" текущую клетку суши, чтобы не посчитать ее снова
        grid[r][e] = '0'

        # Запускаем рекурсию во все 4 стороны
        self.flooding(grid, r + 1, e)
        self.flooding(grid, r - 1, e)
        self.flooding(grid, r, e + 1)
        self.flooding(grid, r, e - 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Если нашли кусок суши — это новый остров
                if grid[i][j] == "1":
                    islands += 1
                    # Запускаем процесс затопления всего найденного острова
                    self.flooding(grid, i, j)

        return islands