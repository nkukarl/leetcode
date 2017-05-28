class Solution(object):
    def max_count(self, m, n, ops):
        x, y = m, n
        for op in ops:
            xx, yy = op
            x = min(x, xx)
            y = min(y, yy)
        return x * y
