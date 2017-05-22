class Solution(object):
    def maximal_square(self, matrix):
        if [] == matrix:
            return 0
        max_area = 0
        col_num = len(matrix[0])
        cur = [0] * col_num
        for row in matrix:
            for i in range(col_num):
                if '1' == row[i]:
                    cur[i] += 1
                else:
                    cur[i] = 0
            max_area = max(max_area, self.get_max_square_area(cur))
        return max_area

    def get_max_square_area(self, heights):
        max_area = 0
        stack = [-1]
        heights.append(0)
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i - stack[-1] - 1
                max_area = max(max_area, min(H, W) ** 2)
            stack.append(i)
        heights.pop()
        return max_area
