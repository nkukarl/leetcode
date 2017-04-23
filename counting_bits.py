class Solution(object):
    def count_bits(self, num):
        base_seq = [0, 1, 1, 2, 1]
        if num <= 4:
            return base_seq[:num + 1]
        power = self.get_power(num)
        bits = [0] + self._count_bits(power)
        return bits[:num + 1]

    def get_power(self, num):
        power = 0
        while num > 0:
            power += 1
            num >>= 1
        return power

    def _count_bits(self, power):
        if power == 2:
            return [1, 1, 2, 1]
        first_half = self._count_bits(power - 1)
        second_half = [b + 1 for b in first_half[:-1]] + [1]
        return first_half + second_half
