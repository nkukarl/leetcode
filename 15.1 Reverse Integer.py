class Solution:
    def reverse(self, n):
        if n == 0:
            return 0
        sign = 1
        if n < 0:
            sign = -1
        n = abs(n)
        ans = 0
        while n:
            ans = ans * 10 + n % 10
            n //= 10

        ans *= sign
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        return ans


n = 2 ** 30

inst = Solution()
print(inst.reverse(n))
