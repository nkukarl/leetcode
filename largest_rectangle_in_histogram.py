class Solution(object):
    def largest_rectangle_area(self, heights):
        max_area = 0
        heights.append(0)
        stack = [-1]
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i - stack[-1] - 1
                max_area = max(max_area, H * W)
            stack.append(i)
        return max_area
