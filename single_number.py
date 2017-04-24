class Solution:
    def single_number_i(self, numbers):
        return self._get_xor(numbers)

    def single_number_iii(self, numbers):
        mark_raw = self._get_xor(numbers)
        mark = 1
        while mark_raw != 0:
            if 1 == mark_raw & 1:
                break
            mark <<= 1
            mark_raw >>= 1
        seq_a, seq_b = [], []
        for n in numbers:
            if 0 == n & mark:
                seq_a.append(n)
            else:
                seq_b.append(n)
        return [self._get_xor(seq_a), self._get_xor(seq_b)]

    def _get_xor(self, numbers):
        xor = 0
        for n in numbers:
            xor ^= n
        return xor