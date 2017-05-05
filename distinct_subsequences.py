class Solution(object):
    def num_distinct(self, s, t):
        m, n = len(s) + 1, len(t) + 1
        dp = [[1] + [0] * (n - 1) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
