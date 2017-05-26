class Solution(object):
    def num_islands(self, grid):
        m = len(grid)
        if 0 == m:
            return 0
        n = len(grid[0])
        if 0 == n:
            return 0
        count = 0
        for i in range(m):
            for j in range(n):
                if '1' == grid[i][j]:
                    count += 1
                    self.destroy(grid, i, j)
        return count

    def destroy(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) \
                or '0' == grid[i][j]:
            return
        grid[i][j] = '0'
        self.destroy(grid, i - 1, j)
        self.destroy(grid, i + 1, j)
        self.destroy(grid, i, j - 1)
        self.destroy(grid, i, j + 1)
