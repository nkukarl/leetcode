from unittest import TestCase

from guess_number_higher_or_lower import Solution


class TestGuessNumberHigherOrLower(TestCase):
    def test_guess_number(self):
        # Setup
        sol = Solution()
        n = 2

        # Exercise
        ans = sol.guess_number(n)

        # Verify
        self.assertEqual(ans, 2)
