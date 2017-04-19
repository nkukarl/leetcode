from unittest import TestCase

from gray_code import Solution


class TestGrayCode(TestCase):
    def test_gray_code(self):
        # Setup
        sol = Solution()
        n = 4

        # Exercise
        ans = sol.gray_code(n)

        # Verify
        self.assertEqual(
            ans,
            [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
        )
