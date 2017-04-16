from unittest import TestCase
from plus_one import Solution


class TestProblemToSolve(TestCase):
    def test_plus_one(self):
        # Setup
        digits = [9, 9, 9]

        sol = Solution()

        # Exercise
        sol.plus_one(digits)

        # Verify
        self.assertEqual(digits, [1, 0, 0, 0])