# DFS: island Problem
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[0])
                or grid[x][y] == "0"
            ):
                return
            grid[x][y] == "0"

            grid(x + 1, y)
            grid(x - 1, y)
            grid(x, y + 1)
            grid(x, y - 1)

        if not grid or grid[0]:  ## boundary: [[]] or grid == "null"
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
