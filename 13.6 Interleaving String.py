class Solution:
    def isInterleave(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = True
        # for row in dp:
        # 	print(row)
        return dp[-1][-1]


s1, s2, s3 = 'aabcc', 'dbbca', 'aadbbcbcac'
# s1, s2, s3 = 'aabcc', 'dbbca', 'aadbbbaccc'

inst = Solution()
print(inst.isInterleave(s1, s2, s3))
