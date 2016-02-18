class Solution:
	def permute(self, A):
		self.res = set()
		self.helper(A, tuple())

		return [list(r) for r in self.res]

	def helper(self, A, cur):
		if not A:
			self.res.add(cur)
		else:
			for i in range(len(A)):
				self.helper(A[:i] + A[i + 1:], cur + (A[i],))

A = [1, 2, 3]

inst = Solution()
print(inst.permute(A))