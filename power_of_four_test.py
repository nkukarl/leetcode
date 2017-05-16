import random
from unittest import TestCase

from power_of_four import Solution


class TestPowerOfFour(TestCase):
    def test_is_power_of_four(self):
        # Setup
        sol = Solution()
        nums = [4 ** i for i in range(16)] + \
               [random.randint(-2 ** 31, 2 ** 31) for _ in range(16)]
        num = random.choice(nums)

        # Exercise
        ans = sol.is_power_of_four(num)

        # Verify
        expected_ans = self.is_power_of_four(num)
        self.assertEqual(ans, expected_ans)

    def is_power_of_four(self, num):
        while num >= 4 and 0 == num % 4:
            num //= 4
        return 1 == num
