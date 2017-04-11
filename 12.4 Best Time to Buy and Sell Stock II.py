class Solution:
    def maxProfit(self, prices):
        profits = [a - b for a, b in zip(prices[1:], prices[:-1])]
        ans = 0
        for p in profits:
            if p > 0:
                ans += p
        return ans


prices = [2, 1, 3, 2, 4, 3]

inst = Solution()
print(inst.maxProfit(prices))
