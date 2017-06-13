class Solution(object):
    def find_words(self, board, words):
        """
        The idea is a bit different from that of word_search question.
        Instead of searching for each word in the board, we are exploring
        the possibilities exist in board instead.
        We start with an empty string as cur and see what words can be formed.
        prefix_set is used to terminate dfs when cur has no possibility to
        be eventually turned into a word in words.
        
        This method is much faster when we have a large word set to investigate.
        
        """
        m = len(board)
        if 0 == m:
            return []
        n = len(board[0])

        self.word_set = set(words)
        self.prefix_set = {''}
        for word in self.word_set:
            for i in range(len(word) - 1):
                self.prefix_set.add(word[:i + 1])

        visited = [[False] * n for _ in range(m)]

        self.ans = set()

        for i in range(m):
            for j in range(n):
                self.explore(board, i, j, '', visited)

        return list(self.ans)

    def explore(self, board, i, j, cur, visited):
        if cur in self.word_set:
            self.ans.add(cur)
        if cur not in self.prefix_set:
            return
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or visited[i][j]:
            return

        visited[i][j] = True

        self.explore(board, i - 1, j, cur + board[i][j], visited)
        self.explore(board, i + 1, j, cur + board[i][j], visited)
        self.explore(board, i, j - 1, cur + board[i][j], visited)
        self.explore(board, i, j + 1, cur + board[i][j], visited)

        visited[i][j] = False
