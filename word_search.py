class Solution(object):
    def exist(self, board, word):
        if '' == word:
            return True
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                if self.explore(board, i, j, word, visited):
                    return True
        return False

    def explore(self, board, i, j, word, visited):
        if '' == word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
                        word[0] != board[i][j] or 1 == visited[i][j]:
            return False
        visited[i][j] = 1
        exist_flag = self.explore(board, i - 1, j, word[1:], visited) or \
                     self.explore(board, i + 1, j, word[1:], visited) or \
                     self.explore(board, i, j - 1, word[1:], visited) or \
                     self.explore(board, i, j + 1, word[1:], visited)
        visited[i][j] = 0
        return exist_flag
