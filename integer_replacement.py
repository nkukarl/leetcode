class Solution(object):
    def integer_replacement(self, n):
        return self.operate(n)

    def operate(self, n):
        if 1 == n:
            return 0
        if 0 == n % 2:
            return 1 + self.operate(n // 2)
        return 1 + min(self.operate(n + 1), self.operate(n - 1))