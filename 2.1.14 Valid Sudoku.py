class Solution:
    def isValidSudoku(self, board):
        m, n = len(board), len(board[0])
        if m != 9 or n != 9:
            return False

        for i in range(m):
            tmp = []
            for j in range(n):
                if board[i][j] != '.':
                    tmp.append(board[i][j])
            print(tmp)
            if len(set(tmp)) != len(tmp):
                return False

        for j in range(n):
            tmp = []
            for i in range(m):
                if board[i][j] != '.':
                    tmp.append(board[i][j])
            print(tmp)
            if len(set(tmp)) != len(tmp):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                tmp = []
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        if board[i + ii][j + jj] != '.':
                            tmp.append(board[i + ii][j + jj])
                print(tmp)
                if len(set(tmp)) != len(tmp):
                    return False

        return True


board = ['53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1',
         '7...2...6', '.6....28.', '...419..5', '....8..79']

inst = Solution()
print(inst.isValidSudoku(board))
