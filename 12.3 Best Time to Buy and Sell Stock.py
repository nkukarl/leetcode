class Solution:
    def maxProfit(self, prices):
        profits = [a - b for a, b in zip(prices[1:], prices[:-1])]
        cur = 0
        ans = 0
        for p in profits:
            cur += p
            if cur <= 0:
                cur = 0
            else:
                ans = max(ans, cur)
        return ans


prices = [2, 1, 3, 2, 4, 3]

inst = Solution()
print(inst.maxProfit(prices))
