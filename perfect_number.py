class Solution(object):
    def check_perfect_number(self, num):
        if num <= 0:
            return False
        sum_ = 1
        SQRT = int(num ** 0.5)
        for i in range(2, SQRT + 1):
            if 0 == num % i:
                sum_ += (i + num // i)
        if SQRT ** 2 == num:
            sum_ -= SQRT
        return sum_ == num
