class Solution(object):
    def generate_matrix(self, n):
        if n < 1:
            return []
        matrix = [[0] * n for _ in range(n)]
        dir = 0
        top = left = 0
        bottom = right = n - 1
        cur = 1
        while top <= bottom and left <= right:
            if 0 == dir % 4:
                cur = self.move_right(cur, matrix, top, left, right)
                top += 1
            elif 1 == dir % 4:
                cur = self.move_down(cur, matrix, right, top, bottom)
                right -= 1
            elif 2 == dir % 4:
                cur = self.move_left(cur, matrix, bottom, left, right)
                bottom -= 1
            elif 3 == dir % 4:
                cur = self.move_up(cur, matrix, left, top, bottom)
                left += 1
            dir += 1
        return matrix

    def move_right(self, cur, matrix, top, left, right):
        for col in range(left, right + 1):
            matrix[top][col] = cur
            cur += 1
        return cur

    def move_down(self, cur, matrix, right, top, bottom):
        for row in range(top, bottom + 1):
            matrix[row][right] = cur
            cur += 1
        return cur

    def move_left(self, cur, matrix, bottom, left, right):
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = cur
            cur += 1
        return cur

    def move_up(self, cur, matrix, left, top, bottom):
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = cur
            cur += 1
        return cur
