class Solution:
	def uniquePaths(self, m, n):
		dp = [[1] * n for _ in range(m)]
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[-1][-1]

m, n = 3, 7

inst = Solution()
print(inst.uniquePaths(m, n))