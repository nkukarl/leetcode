class Solution:
    def climbing_stairs(self, n):
        if type(n) != int or n <= 0:
            raise ValueError
        if n <= 2:
            return n
        a, b = 1, 2
        while n - 2:
            a, b = b, a + b
            n -= 1
        return b
