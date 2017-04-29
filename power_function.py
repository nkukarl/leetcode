class Solution(object):
    def power_function(self, x, n):
        if 0 == n or 1 == x:
            return 1
        flag = False
        if n < 0:
            n *= -1
            flag = True
        ans = self.calc(x, n)
        if flag:
            return 1.0 / ans
        return ans

    def calc(self, x, n):
        if n == 1:
            return x
        m = n // 2
        ans_ = self.calc(x, m)
        ans = ans_ * ans_
        if n % 2 == 1:
            ans *= x
        return ans
