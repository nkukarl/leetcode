class Solution(object):
    def min_distance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[i for i in range(n + 1)]] + \
             [[i] + [0] * n for i in range(1, m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] != word2[j - 1]:
                    diff = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    diff = dp[i - 1][j - 1]
                dp[i][j] = diff
        return dp[-1][-1]
