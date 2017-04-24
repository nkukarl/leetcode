from unittest import TestCase

from ugly_number import Solution


class TestUglyNumber(TestCase):
    def test_is_ugly(self):
        # Setup
        sol = Solution()
        num = 125

        # Exercise
        ans = sol.is_ugly(num)

        # Verify
        self.assertTrue(ans)
