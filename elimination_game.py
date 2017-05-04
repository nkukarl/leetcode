class Solution(object):
    def last_remaining(self, n):
        start, count, step = 1, n, 1
        while count > 1:
            end = start + (count - 1) * step
            # compute the next round
            start = end - (count % 2) * step
            count //= 2
            step *= -2
        return start
