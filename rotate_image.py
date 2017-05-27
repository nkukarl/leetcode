class Solution(object):
    def rotate(self, matrix):
        """
        The most pythonic way to rotate an matrix by 90 degrees clockwise
        rotated = [list(row) for row in zip(*matrix[::-1])]
        """
        n = len(matrix)
        if n < 2:
            return

        # Top-bottom mirror
        top, bottom = 0, n - 1
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1

        # Diagonal mirror
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
