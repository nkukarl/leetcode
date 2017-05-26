class Solution(object):
    def spiral_order(self, matrix):
        m = len(matrix)
        if 0 == m:
            return []
        n = len(matrix[0])
        if 0 == n:
            return []
        self.matrix = matrix
        self.top, self.bottom = 0, m - 1
        self.left, self.right = 0, n - 1

        self.ans = []
        dir = 0
        while self.top <= self.bottom and self.left <= self.right:
            if 0 == dir % 4:
                self.move_right()
                self.top += 1
            elif 1 == dir % 4:
                self.move_down()
                self.right -= 1
            elif 2 == dir % 4:
                self.move_left()
                self.bottom -= 1
            elif 3 == dir % 4:
                self.move_up()
                self.left += 1
            dir += 1

        return self.ans

    def move_right(self):
        for col in range(self.left, self.right + 1):
            self.ans.append(self.matrix[self.top][col])

    def move_down(self):
        for row in range(self.top, self.bottom + 1):
            self.ans.append(self.matrix[row][self.right])

    def move_left(self):
        for col in range(self.right, self.left - 1, -1):
            self.ans.append(self.matrix[self.bottom][col])

    def move_up(self):
        for row in range(self.bottom, self.top - 1, -1):
            self.ans.append(self.matrix[row][self.left])
