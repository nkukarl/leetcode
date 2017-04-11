class Solution:
    def spiralOrder(self, M):
        m, n = len(M), len(M[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        direction = 0
        ans = []
        while top <= bottom and left <= right:
            if direction == 0:
                for j in range(left, right + 1):
                    ans.append(M[top][j])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    ans.append(M[i][right])
                right -= 1
            elif direction == 2:
                for j in range(right, left - 1, -1):
                    ans.append(M[bottom][j])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ans.append(M[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = [[1, 2], [3, 4]]
M = [[1]]
M = [[1, 2, 3], [4, 5, 6]]

inst = Solution()
print(inst.spiralOrder(M))
