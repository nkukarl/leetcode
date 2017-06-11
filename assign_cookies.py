class Solution(object):
    def find_content_children(self, greed_levels, sizes):
        greed_levels.sort()
        sizes.sort()
        m = len(greed_levels)
        count = 0
        for size in sizes:
            if count == m:
                return count
            if size >= greed_levels[count]:
                count += 1
        return count
