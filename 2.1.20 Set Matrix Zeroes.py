class Solution:
	def setZeroes(self, M):
		m, n = len(M), len(M[0])
		rows = [False] * m
		cols = [False] * n
		for i in range(m):
			for j in range(n):
				if M[i][j] == 0:
					rows[i] = cols[j] = True

		for i in range(m):
			if rows[i]:
				for j in range(n):
					M[i][j] = 0

		for j in range(n):
			if cols[j]:
				for i in range(m):
					M[i][j] = 0

M = [[1, 2, 0, 1], [2, 3, 1, 0], [0, 3, 2, 1], [1, 1, 1, 1]]

inst = Solution()
inst.setZeroes(M)

print(M)