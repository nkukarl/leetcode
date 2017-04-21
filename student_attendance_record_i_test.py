from unittest import TestCase

from student_attendance_record_i import Solution


class TestCheckRecord(TestCase):
    def test_check_record(self):
        # Setup
        sol = Solution()
        s = 'LPLLPALLP'

        # Exercise
        ans = sol.check_record(s)

        # Verify
        self.assertTrue(ans)
