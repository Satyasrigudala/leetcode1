class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n

        # Flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Shift using modulo
        k = k % total
        flat = flat[-k:] + flat[:-k]

        # Reshape back to 2D
        new_grid = [[flat[i*n + j] for j in range(n)] for i in range(m)]
        return new_grid
        
