class Solution(object):
    def count_primes(self, n):
        if n <= 2:
            return 0
        seq = [0] * 2 + [1] * (n - 2)
        for i in range(2, n):
            if 1 == seq[i]:
                x = 2 * i
                while x <= n - 1:
                    seq[x] = 0
                    x += i
        return sum(seq)
