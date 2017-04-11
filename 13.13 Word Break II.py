class Solution:
    def wordBreak(self, s, Dict):
        if not s or not Dict:
            return []

        self.Dict = Dict
        self.res = []

        self.helper(s, [])

        return self.res

    def helper(self, s, cur):
        if not s:
            return self.res.append(cur)
        for word in self.Dict:
            if len(s) >= len(word) and s[:len(word)] == word:
                self.helper(s[len(word):], cur + [word])


s = 'catsanddogs'
Dict = ['cat', 'cats', 'and', 'sand', 'dog', 'dogs', 's']

inst = Solution()
print(inst.wordBreak(s, Dict))
