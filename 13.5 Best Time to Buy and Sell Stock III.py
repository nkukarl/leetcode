class Solution:
	def maxProfit(self, prices):
		profits = [a - b for a, b in zip(prices[1:], prices[:-1])]
		l2r = self.helper(profits)
		r2l = self.helper(profits[::-1])[::-1]

		l2r.insert(0, 0)
		r2l.append(0)

		ans = 0

		for i in range(len(l2r)):
			ans = max(ans, l2r[i] + r2l[i])

		return ans
		
	def helper(self, profits):
		curP = []
		cur = 0
		maxP = 0
		for p in profits:
			cur += p
			if cur <= 0:
				cur = 0	
			maxP = max(maxP, cur)
			curP.append(maxP)
		return curP

prices = [1, 2, 1, 3, 7, 1]
prices = [2, 1, 2, 0, 1]

inst = Solution()
print(inst.maxProfit(prices))
