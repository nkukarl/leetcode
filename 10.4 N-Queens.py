class Solution:
	def solveNQueens(self, n):
		self.n = n
		self.res = []
		self.helper([])

		return self.res

	def helper(self, cur):
		if len(cur) == self.n:
			self.res.append(cur)
		else:
			r = len(cur)
			tmp = '.' * self.n
			for c in range(self.n):
				if self.check(cur, r, c):
					self.helper(cur + [tmp[:c] + 'Q' + tmp[c + 1:]])

	def check(self, cur, r, c):
		for rr in range(r):
			if cur[rr][c] == 'Q':
				return False
		rr, cc = r - 1, c - 1
		while rr >= 0 and cc >= 0:
			if cur[rr][cc] == 'Q':
				return False
			rr -= 1
			cc -= 1
		rr, cc = r - 1, c + 1
		while rr >= 0 and cc < self.n:
			if cur[rr][cc] == 'Q':
				return False
			rr -= 1
			cc += 1
		return True

n = 8

inst = Solution()
ans = inst.solveNQueens(n)
for i in range(len(ans)):
	print(i + 1)
	for row in ans[i]:
		print(row)
	print()