class Solution(object):
    def min_path_sum(self, grid):
        m, n = len(grid), len(grid[0])
        cost = [[0] * n for _ in range(m)]

        cost_top_row = 0
        for c in range(n):
            cost_top_row += grid[0][c]
            cost[0][c] = cost_top_row

        cost_left_col = 0
        for r in range(m):
            cost_left_col += grid[r][0]
            cost[r][0] = cost_left_col

        for r in range(1, m):
            for c in range(1, n):
                cost[r][c] = min(cost[r][c - 1], cost[r - 1][c]) + grid[r][c]

        return cost[-1][-1]