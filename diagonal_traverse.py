class Solution(object):
    def find_diagonal_order(self, matrix):
        if [] == matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        if 1 == m:
            return matrix[0]
        if 1 == n:
            return [r[0] for r in matrix]

        flag = -1
        ans = []
        for i in range(m + n):
            cur = []
            for j in range(i + 1):
                xx, yy = j, i - j
                if xx < m and yy < n:
                    cur.append(matrix[xx][yy])
            if -1 == flag:
                ans.extend(cur[::-1])
            else:
                ans.extend(cur)
            flag *= -1

        return ans
