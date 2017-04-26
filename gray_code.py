class Solution:
    def gray_code(self, n):
        if 0 == n:
            return [0]
        first_half = self.gray_code(n - 1)
        second_half = [x + 2 ** (n - 1) for x in first_half[::-1]]

        return first_half + second_half
