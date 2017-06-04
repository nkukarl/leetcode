class Solution(object):
    def largest_palindrome(self, digit):
        # Handle simple scenario
        if 1 == digit:
            return 9

        max_n = int('9' * digit)
        min_n = int('1' + '0' * (digit - 1))

        left = int(str(max_n ** 2)[:digit])
        right = int(str(max_n ** 2)[digit:])
        if right < left:
            left -= 1
        for n_raw in range(left, min_n - 1, -1):
            prod = int(str(n_raw) + str(n_raw)[::-1])
            for n in range(max_n, int(prod ** 0.5) - 1, -1):
                if prod % n == 0:
                    return prod % 1337
        # Actually, there is one more thing needs to be solved.
        # For example, if digit = 2, we have only considered numbers like
        # XYYX but not numbers like XYX.
        # However, we have already obtained a larger product.
