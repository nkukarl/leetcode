class Solution(object):
    def trailing_zeros(self, n):
        if n < 5:
            return 0
        bits = 2
        weight = 5
        while weight <= n:
            bits += 1
            weight *= 5
        bits -= 1
        weight //= 5
        base_5 = []
        for i in range(bits):
            base_5.append(n // weight)
            n %= weight
            weight //= 5
        counts = self.get_counts(bits)
        return sum([val * count for val, count in zip(base_5, counts)])

    def get_counts(self, bits):
        counts = [0]
        for i in range(1, bits):
            counts.append(counts[-1] * 5 + 1)
        return counts[::-1]
