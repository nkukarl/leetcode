class Solution(object):
    def divide(self, dividend, divisor):
        OVERFLOW = -1
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1
        if 0 == divisor:
            return OVERFLOW
        sign = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        weight = 1
        while dividend >= divisor:
            divisor <<= 1
            weight <<= 1
        divisor >>= 1
        weight >>= 1
        ans = 0
        while weight > 0 and dividend != 0:
            if dividend >= divisor:
                ans += weight
                dividend -= divisor
            weight >>= 1
            divisor >>= 1
        if -1 == sign:
            ans = -ans
        if ans > MAX_INT:
            return MAX_INT
        if ans < MIN_INT:
            return MIN_INT
        return ans