class Solution:
	def combinationSumII(self, A, target):
		A.sort()
		self.target = target
		self.res = set()
		self.helper(A, tuple())

		return [list(r) for r in self.res]

	def helper(self, A, cur):
		if sum(cur) == self.target:
			self.res.add(cur)
		elif sum(cur) < self.target:
			for i in range(len(A)):
				self.helper(A[i + 1:], cur + (A[i], ))

A = [10, 1, 2, 7, 6, 1, 5]
target = 8

inst = Solution()
print(inst.combinationSumII(A, target))