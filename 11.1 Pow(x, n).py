class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        res = self.helper(x, abs(n))
        if n < 0:
            return 1 / res
        return res

    def helper(self, x, n):
        if n == 1:
            return x
        tmp = self.helper(x, n // 2)
        ans = tmp ** 2
        if n % 2 == 1:
            ans *= x
        return ans


x, n = 21, 11
inst = Solution()
print(inst.myPow(x, n), x ** n)
