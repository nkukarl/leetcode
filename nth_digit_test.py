import random
from unittest import TestCase

from nth_digit import Solution


class TestNthDigit(TestCase):
    def test_find_nth_digit(self):
        # Setup
        sol = Solution()
        n = random.randint(1, 2 ** 20)

        # Exercise
        ans = sol.find_nth_digit(n)

        # Verify
        expected_ans = self.find_nth_digit(n)
        self.assertEqual(ans, expected_ans)

    def find_nth_digit(self, n):
        digits = ''
        for i in range(1, 1111111):
            digits += str(i)
        return int(digits[n - 1])
