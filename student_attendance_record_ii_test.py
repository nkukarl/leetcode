import itertools
from unittest import TestCase

from student_attendance_record_ii import Solution


class TestCheckRecord(TestCase):
    def test_check_record(self):
        # Setup
        sol = Solution()
        n = 100000

        # Exercise
        ans = sol.check_record(n)

        # Verify
        self.assertEqual(ans, 749184020)

    def test_calc_a_seq(self):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.calc_a_seq(20)

        # Verify
        self.assertEqual(ans[-1], 223317)


