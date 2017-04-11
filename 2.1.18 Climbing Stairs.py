class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        while n - 2:
            a, b = b, a + b
            n -= 1
        return b


inst = Solution()
print(inst.climbStairs(5))
