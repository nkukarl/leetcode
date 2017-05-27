class Solution(object):
    def find_content_children(self, greed_levels, cookie_sizes):
        i = j = 0
        greed_levels.sort()
        cookie_sizes.sort()
        m, n = len(greed_levels), len(cookie_sizes)
        while i < m and j < n:
            if greed_levels[i] <= cookie_sizes[j]:
                i += 1
            j += 1
        return i
