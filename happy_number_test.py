from unittest import TestCase

from happy_number import Solution


class TestHappyNumber(TestCase):
    def test_is_happy(self):
        # Setup
        sol = Solution()
        n = 19  # True
        # n = 333  # False

        # Exercise
        ans = sol.is_happy(n)

        # Verify
        self.assertTrue(ans)
