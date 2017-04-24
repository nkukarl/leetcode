class Solution(object):
    def is_happy(self, n):
        cache = set()
        while True:
            n = self.calc_next(n)
            if 1 == n:
                return True
            if n in cache:
                return False
            cache.add(n)

    def calc_next(self, n):
        ans = 0
        while n != 0:
            ans += (n % 10) ** 2
            n //= 10
        return ans
