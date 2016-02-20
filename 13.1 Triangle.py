class Solution:
	def minimumTotal(self, triangle):
		m = len(triangle)
		dp = [[0] * i for i in range(1, m + 1)]
		dp[0][0] = triangle[0][0]
		for i in range(1, m):
			for j in range(i + 1):
				if j == 0:
					dp[i][j] = dp[i - 1][0] + triangle[i][j]
				elif j == i:
					dp[i][j] = dp[i - 1][-1] + triangle[i][j]
				else:
					dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
		print(dp)
		return min(dp[-1])

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

inst = Solution()
print(inst.minimumTotal(triangle))