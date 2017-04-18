from unittest import TestCase
from plus_one import Solution
import random


class TestProblemToSolve(TestCase):
    def test_plus_one(self):
        # Setup
        number = random.randint(1, 1000)

        digits = list(map(int, str(number)))
        expected_digits = list(map(int, str(number + 1)))

        sol = Solution()

        # Exercise
        sol.plus_one(digits)

        # Verify
        self.assertEqual(digits, expected_digits)