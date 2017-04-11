class Solution:
    def wordBreak(self, s, Dict):
        if not s:
            return True
        if not Dict:
            return False
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for word in Dict:
                if s[i - len(word): i] == word and dp[i - len(word)]:
                    dp[i] = True
        return dp[-1]


s = 'leetcode'
Dict = ['leet', 'code']

inst = Solution()
print(inst.wordBreak(s, Dict))
