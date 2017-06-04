class Solution(object):
    def word_break(self, s, word_dict):
        m = len(s)
        dp = [True] + [False] * m

        for i in range(m):
            for j in range(m):
                if dp[i]:
                    word = s[i: j + 1]
                    if word in word_dict:
                        dp[j + 1] = True
        return dp[-1]
