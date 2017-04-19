class Solution:
    def unique_paths_with_obstacles(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # Apparently, if there is an obstacle at the starting point,
        # the number of paths would be 0.
        if 1 == grid[0][0]:
            return 0
        # If there is no obstacles at the starting point,
        # the number of unique paths to the starting point is 1.
        dp[0][0] = 1
        # For each point in the top row and leftmost column, its unique paths
        # depends on whether there is obstacle before it and whether there
        # are obstacles there. If it is accessible, the maximum number of
        # paths would be 1. Otherwise, it is 0.
        for i in range(1, m):
            if 0 == grid[i][0]:
                dp[i][0] = 1
            else:
                break
        for j in range(1, n):
            if 0 == grid[0][j]:
                dp[0][j] = 1
            else:
                break
        # For each point not in the top row or leftmost column, similar approach
        # as in unique_path.py can be used. The only difference is that if there
        # are obstacles there, the points are not accessible, the number of
        # paths is zero.
        for i in range(1, m):
            for j in range(1, n):
                if 0 == grid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
