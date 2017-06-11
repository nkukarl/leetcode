class Solution(object):
    """
    lookup_tbl = {
        0: 1,
        1: 10,
        2: 91,
        3: 739,
        4: 5275,
        5: 32491,
        6: 168571,
        7: 712891,
        8: 2345851,
        9: 5611771,
        10: 8877691,
    }
    """

    def count_numbers_with_unique_digits(self, n):
        n = min(n, 10)
        return sum([self.count_n_digits(i) for i in range(n + 1)])

    def count_n_digits(self, n):
        if n == 0:
            return 1
        count = 9
        base = 9
        for i in range(n - 1):
            count *= base
            base -= 1
        return count
