class Solution(object):
    def generate_parentheses(self, n):
        self.ans = []
        self.generate(n, n, '')
        return self.ans

    def generate(self, l, r, cur):
        if l > r:
            return
        if 0 == r:
            self.ans.append(cur)
        else:
            if l >= 1:
                self.generate(l - 1, r, cur + '(')
            if r >= 1:
                self.generate(l, r - 1, cur + ')')
