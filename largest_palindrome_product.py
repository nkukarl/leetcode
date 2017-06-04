# TODO: Fix TLE
class Solution(object):
    def largest_palindrome(self, digit):
        max_n = int('9' * digit)
        min_n = int('1' + '0' * (digit - 1))

        max_prod = max_n ** 2
        min_prod = min_n ** 2
        for prod in range(max_prod, min_prod - 1, -1):
            if not self.is_palindrome(prod):
                continue
            for n in range(max_n, int(prod ** 0.5) - 1, -1):
                if prod % n == 0:
                    return prod % 1337

    def is_palindrome(self, prod):
        prod_str = str(prod)
        left, right = 0, len(prod_str) - 1
        while left < right:
            if prod_str[left] != prod_str[right]:
                return False
            left += 1
            right -= 1
        return True