class Solution:
	def solveSudoku(self, board):
		self.helper(board, 0)
		return self.res

	def helper(self, board, cur):
		if cur == 81:
			self.res = board
		else:
			i, j = cur // 9, cur % 9
			if board[i][j] == '.':
				for k in range(1, 10):
					tmp = board[:i] + [board[i][:j] + [k] + board[i][j + 1:]] + board[i + 1:]
					if self.isValidSudoku(tmp):
						self.helper(tmp, cur + 1)
					else:
						continue
			else:
				self.helper(board, cur + 1)

	def isValidSudoku(self, board):
		m, n = len(board), len(board[0])
		if m != 9 or n != 9:
			return False

		for i in range(m):
			tmp = []
			for j in range(n):
				if board[i][j] != '.':
					tmp.append(board[i][j])
			# print(tmp)
			if len(set(tmp)) != len(tmp):
				return False

		for j in range(n):
			tmp = []
			for i in range(m):
				if board[i][j] != '.':
					tmp.append(board[i][j])
			# print(tmp)
			if len(set(tmp)) != len(tmp):
				return False

		for i in [0, 3, 6]:
			for j in [0, 3, 6]:
				tmp = []
				for ii in range(0, 3):
					for jj in range(0, 3):
						if board[i + ii][j + jj] != '.':
							tmp.append(board[i + ii][j + jj])
				# print(tmp)
				if len(set(tmp)) != len(tmp):
					return False

		return True

board = [[5,3,'.','.',7,'.','.','.','.'], [6,'.','.',1,9,5,'.','.','.'], ['.',9,8,'.','.','.','.',6,'.'], [8,'.','.','.',6,'.','.','.',3], [4,'.','.',8,'.',3,'.','.',1], [7,'.','.','.',2,'.','.','.',6], ['.',6,'.','.','.','.',2,8,'.'], ['.','.','.',4,1,9,'.','.',5], ['.','.','.','.',8,'.','.',7,9]]

inst = Solution()
res = inst.solveSudoku(board)

for row in res:
	print(row)