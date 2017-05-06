import random
from unittest import TestCase

from divide_two_integers import Solution


class TestDivideTwoIntegers(TestCase):
    def test_divide(self):
        # Setup
        sol = Solution()
        dividend = random.randint(-1000, 1000)
        divisor = random.randint(-1000, 1000)
        # dividend = -950
        # divisor = 140

        # Exercise
        ans = sol.divide(dividend, divisor)
        sign = 1 if dividend * divisor >= 0 else -1
        expected_ans = abs(dividend) // abs(divisor) * sign

        # Verify
        self.assertEqual(ans, expected_ans)
