class Solution:
    def gray_code(self, n):
        if type(n) != int or n < 1:
            raise ValueError
        if 1 == n:
            return [0, 1]
        first_half = self.gray_code(n - 1)
        second_half = [x + 2 ** (n - 1) for x in reversed(first_half)]

        return first_half + second_half
