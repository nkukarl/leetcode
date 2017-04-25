import random
from unittest import TestCase

from plus_one import Solution


class TestPlusOne(TestCase):
    def test_plus_one(self):
        # Setup
        sol = Solution()
        number = random.randint(1, 1000)
        digits = list(map(int, str(number)))

        # Exercise
        sol.plus_one(digits)

        # Verify
        expected_digits = list(map(int, str(number + 1)))
        self.assertEqual(digits, expected_digits)
