class Solution:
    def generateMatrix(self, n):
        M = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        cur = 1
        direction = 0
        while top <= bottom and left <= bottom:
            if direction == 0:
                for j in range(left, right + 1):
                    M[top][j] = cur
                    cur += 1
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    M[i][right] = cur
                    cur += 1
                right -= 1
            elif direction == 2:
                for j in range(right, left - 1, -1):
                    M[bottom][j] = cur
                    cur += 1
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    M[i][left] = cur
                    cur += 1
                left += 1
            direction = (direction + 1) % 4
        return M


inst = Solution()
print(inst.generateMatrix(4))
