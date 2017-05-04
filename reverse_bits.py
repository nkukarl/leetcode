class Solution:
    def reverse_bits(self, n):
        count = 32
        weight = 2 ** 31
        ans = 0
        while count > 0:
            ans += (n & 1) * weight
            weight //= 2
            count -= 1
            n >>= 1
        return ans
