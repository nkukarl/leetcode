from unittest import TestCase

from student_attendance_record_ii import Solution


class TestCheckRecord(TestCase):
    def test_check_record(self):
        # Setup
        sol = Solution()
        n = 99999

        # Exercise
        ans = sol.check_record(n)

        # Verify
        self.assertEqual(ans, 816671055)
