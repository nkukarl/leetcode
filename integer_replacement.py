class Solution(object):
    def integer_replacement(self, n):
        self.DICT = {}
        return self.operate(n)

    def operate(self, n):
        if 1 == n:
            return 0
        if n not in self.DICT:
            if 0 == n % 2:
                self.DICT[n] = 1 + self.operate(n // 2)
            else:
                self.DICT[n] = 1 + min(self.operate(n + 1), self.operate(n - 1))
        return self.DICT[n]