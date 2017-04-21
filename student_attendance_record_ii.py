import itertools


class Solution(object):
    def check_record(self, n):
        return self.calc_f_seq(n) % (10 ** 9 + 7)

    def calc_f_seq(self, n):
        base_val = [1, 3, 8, 19]
        if n <= 3:
            return base_val[n]
        a_seq = self.calc_a_seq(n - 1)
        counter = 0
        while counter + 3 < n:
            base_val.append(
                base_val[-1] * 2 - base_val[-4] +
                a_seq[counter + 3] - a_seq[counter])
            counter += 1
            base_val = base_val[1:]
        return base_val[-1]

    def calc_a_seq(self, n):
        base_val = [1, 2, 4, 7]
        while n > 3:
            base_val.append(base_val[-1] * 2 - base_val[-4])
            n -= 1
        return base_val
