class Solution(object):
    def check_record(self, n):
        """
        How to form n X...X from (n - 1) X...X

        * append P
            Any sequence

            => seq(n - 1)

        * append A
            Any sequence without A
            lp_seq(n) = lp_seq(n - 1) + lp_seq(n - 2) + lp_seq(n - 3)
                * (n - 1) X...X ends with P
                * (n - 1) X...X ends with PL
                * (n - 2) X...X ends with PLL
            lp_seq(0) = 1
            lp_seq(1) = 2
            lp_seq(2) = 4
            lp_seq(3) = 7

            => lp_seq(n - 1)

        * append L
            Any sequence not ends with LL
                (n - 4) X...X + P + LL
                    seq(n - 4)
                (n - 4) X...X + A + LL
                    lp_seq(n - 4)

            => seq(n - 1) - seq(n - 4) - lp_seq(n - 4)


        seq(n) = 2 * seq(n - 1) - seq(n - 4) + lp_seq(n - 1) - lp_seq(n - 4)

        seq(0) = 1
        seq(0) = 3
        seq(0) = 8
        seq(0) = 19

        """
        # Base sequence to start with
        seq = [1, 3, 8, 19]

        # Simple case
        if n <= 3:
            return seq[n]

        # Modulo base
        M = 10 ** 9 + 7

        # Calculate sequence without A (with only L and P)
        m = n - 1
        lp_seq = [1, 2, 4, 7]
        while m > 3:
            lp_seq.append(sum(lp_seq[-3:]) % M)
            m -= 1

        # Calculate sequence
        counter = 0
        while counter + 3 < n:
            seq.append((seq[-1] * 2 - seq[-4] +
                        lp_seq[counter + 1] + lp_seq[counter + 2]) % M)
            counter += 1
        return seq[-1]
