class Solution(object):
    def solve(self, board):
        m = len(board)
        if m < 3:
            return
        n = len(board[0])
        if n < 3:
            return

        self.handle_edges(board)

        for i in range(m):
            for j in range(n):
                if 'O' == board[i][j]:
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if '$' == board[i][j]:
                    board[i][j] = 'O'

    def handle_edges(self, board):
        m, n = len(board), len(board[0])
        for row in [0, m - 1]:
            for col in range(n):
                self.mark(board, row, col)
        for row in range(m):
            for col in [0, n - 1]:
                self.mark(board, row, col)

    def mark(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) \
                or board[i][j] != 'O':
            return
        board[i][j] = '$'
        self.mark(board, i - 1, j)
        self.mark(board, i + 1, j)
        self.mark(board, i, j - 1)
        self.mark(board, i, j + 1)
