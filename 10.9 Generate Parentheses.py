class Solution:
    def generateParentheses(self, n):
        self.res = []
        self.helper(n, n, '')

        return self.res

    def helper(self, left, right, cur):
        if right < left:
            return
        if left == right == 0:
            self.res.append(cur)
        if left > 0:
            self.helper(left - 1, right, cur + '(')
        if right > 0:
            self.helper(left, right - 1, cur + ')')


n = 3

inst = Solution()
print(inst.generateParentheses(n))
