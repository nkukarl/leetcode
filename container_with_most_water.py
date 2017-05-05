class Solution(object):
    def get_max_area(self, heights):
        max_area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            h_left, h_right = heights[left], heights[right]
            area = min(h_left, h_right) * (right - left)
            max_area = max(max_area, area)
            if h_left == h_right:
                left += 1
                right -= 1
            elif h_left < h_right:
                left += 1
            else:
                right -= 1
        return max_area
