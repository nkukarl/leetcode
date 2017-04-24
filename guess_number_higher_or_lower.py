def guess(num):
    N = 2
    if N == num:
        return 0
    if num > N:
        return -1
    return 1


class Solution(object):
    def guess_number(self, n):
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            resp = guess(mid)
            if 0 == resp:
                return mid
            if -1 == resp:
                high = mid
            else:
                low = mid + 1
        return high
