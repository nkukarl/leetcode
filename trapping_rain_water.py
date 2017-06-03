class Solution(object):
    def trap(self, heights):
        # Handle simple scenario
        if len(heights) < 3:
            return 0

        L = self.get_max_height_to_one_side(heights)
        R = self.get_max_height_to_one_side(heights[::-1])[::-1]
        ans = 0
        for h, l, r in zip(heights, L, R):
            H = min(l, r)
            ans += max(0, H - h)
        return ans

    def get_max_height_to_one_side(self, heights):
        L = [0]
        max_height = 0
        for i in range(1, len(heights)):
            if heights[i - 1] > max_height:
                max_height = heights[i - 1]
            L.append(max_height)
        return L
