class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, visited, word):
                    return True
        return False

    def helper(self, board, i, j, visited, word):
        if not word:
            return True
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if visited[i][j]:
            return False
        if board[i][j] != word[0]:
            return False
        visited[i][j] = True
        tmp = self.helper(board, i - 1, j, visited, word[1:]) or self.helper(
            board, i + 1, j, visited, word[1:]) or self.helper(board, i, j - 1,
                                                               visited, word[
                                                                        1:]) or self.helper(
            board, i, j + 1, visited, word[1:])
        visited[i][j] = False
        return tmp


board = ['ABCE', 'SFCS', 'ADEE']

word = 'ABCCED'
# word = 'SEE'
# word = 'ABCB'
word = 'ABCESEEDASFC'

inst = Solution()
print(inst.exist(board, word))
