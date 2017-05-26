class Solution(object):
    def search_matrix(self, matrix, target):
        m = len(matrix)
        if 0 == m:
            return False
        n = len(matrix[0])
        if 0 == n:
            return False

        i, j = m - 1, 0
        while i >= 0 and j < n:
            cur = matrix[i][j]
            if cur == target:
                return True
            if cur > target:
                i -= 1
            else:
                j += 1
        return False
