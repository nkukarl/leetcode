class Solution(object):
    def super_pow(self, a, b):
        if 1 == a:
            return 1
        n = int(''.join(map(str, b)))
        a %= 1337
        return self.get_power(a, n)

    def get_power(self, a, n):
        if 1 == n:
            return a % 1337
        m = n // 2
        ans_ = self.get_power(a, m)
        ans = ans_ * ans_
        if 1 == n % 2:
            ans *= a
        return ans % 1337
