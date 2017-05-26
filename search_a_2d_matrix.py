class Solution(object):
    def search_matrix(self, matrix, target):
        m = len(matrix)
        if 0 == m:
            return False
        n = len(matrix[0])
        if 0 == n:
            return False

        top, bottom = 0, m - 1
        while top < bottom:
            row_id = (top + bottom) // 2
            if target > matrix[row_id][-1]:
                top = row_id + 1
            else:
                bottom = row_id
        row_id = top

        left, right = 0, n - 1
        while left < right:
            col_id = (left + right) // 2
            if target > matrix[row_id][col_id]:
                left = col_id + 1
            else:
                right = col_id
        col_id = left

        return matrix[row_id][col_id] == target
