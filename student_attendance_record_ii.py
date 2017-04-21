class Solution(object):
    def check_record(self, n):
        seq = [1, 3, 8, 19]
        if n <= 3:
            return seq[n]
        lp_only_seq = [1, 2, 4, 7]
        while n > 3:
            seq.append(
                seq[-1] * 2 - seq[-4] +
                lp_only_seq[-1] - lp_only_seq[-4])
            seq.pop(0)
            n -= 1
            lp_only_seq.append(lp_only_seq[-1] * 2 - lp_only_seq[-4])
            lp_only_seq.pop(0)
        return seq[-1] % (10 ** 9 + 7)
