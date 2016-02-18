class Solution:
	def uniquePathsWithObstacles(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [[0] * n for _ in range(m)]
		if grid[0][0] == 1:
			return 0
		dp[0][0] = 1
		for i in range(1, m):
			if grid[i][0] == 0:
				dp[i][0] = 1
			else:
				break
		for j in range(1, n):
			if grid[0][j] == 0:
				dp[0][j] = 1
			else:
				break
		for i in range(1, m):
			for j in range(1, n):
				if grid[i][j] == 0:
					dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
				else:
					dp[i][j] = 0
		return dp[-1][-1]

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

inst = Solution()
print(inst.uniquePathsWithObstacles(grid))
