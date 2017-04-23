import random
from unittest import TestCase

from student_attendance_record_ii import Solution


class TestCheckRecord(TestCase):
    def check_record(self, n):
        seq = [1, 3, 8, 19]
        if n <= 3:
            return seq[n]
        lp_seq = [1, 2, 4, 7]
        M = 10 ** 9 + 7
        while n > 3:
            seq.append((seq[-1] * 2 - seq[-4] + sum(lp_seq[-3:-1])) % M)
            n -= 1
            lp_seq.append(sum(lp_seq[-3:]) % M)
        return seq[-1] % M

    def test_check_record(self):
        # Setup
        sol = Solution()
        n = random.randint(1, 100000)

        # Exercise
        ans = sol.check_record(n)
        expected_ans = self.check_record(n)

        # Verify
        self.assertEqual(ans, expected_ans)
