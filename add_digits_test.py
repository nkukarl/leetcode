import random
from unittest import TestCase

from add_digits import Solution


class TestAddDigits(TestCase):
    def test_add_digits(self):
        # Setup
        sol = Solution()
        num = random.randint(100, 1000)

        # Exercise
        ans = sol.add_digits(num)
        expected_ans = self.add_digits(num)

        # Verify
        self.assertEqual(ans, expected_ans)

    def add_digits(self, num):
        while num >= 10:
            num = self.calc(num)
        return num

    def calc(self, num):
        ans = 0
        while num >= 10:
            ans += num % 10
            num //= 10
        return ans + num
