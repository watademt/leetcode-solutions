# https://leetcode.com/problems/rotting-oranges/
# Сложность: Medium
# Тема: Array / Breadth-First Search / Matrix

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh_count = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0

        while queue and fresh_count > 0:
            level_size = len(queue)

            for _ in range(level_size):
                org = queue.popleft()

                for dr, dc in directions:
                    new_r = org[0] + dr
                    new_c = org[1] + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        queue.append((new_r, new_c))

            minutes += 1

        if fresh_count == 0:
            return minutes
        else:
            return -1