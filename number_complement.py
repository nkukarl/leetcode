class Solution(object):
    def find_complement(self, num):
        if 0 == num:
            return 1
        total = 0
        cur_val = 1
        n = num
        while n:
            total += cur_val
            cur_val <<= 1
            n >>= 1
        return total - num
