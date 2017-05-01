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
        n = n if n <= 10 else 10
        self.factorials = self.get_factorials()
        return self.count_numbers(n)

    def count_numbers(self, n):
        if n == 0:
            return 1
        count_ = self.count_numbers(n - 1)
        return self.count_permutation(9, n - 1) * 9 + count_

    def count_permutation(self, n, k):
        return self.factorials[n] // self.factorials[n - k]

    def get_factorials(self):
        factorials = [1]
        for n in range(1, 10):
            factorials.append(factorials[-1] * n)
        return factorials
