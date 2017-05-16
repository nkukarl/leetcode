import random
from unittest import TestCase

from power_of_three import Solution


class TestPowerOfThree(TestCase):
    def test_is_power_of_three(self):
        # Setup
        sol = Solution()
        nums = [3 ** i for i in range(19)] + \
               [random.randint(-2 ** 31, 2 ** 31) for _ in range(19)]
        num = random.choice(nums)

        # Exercise
        ans = sol.is_power_of_three(num)

        # Verify
        expected_ans = self.is_power_of_three(num)
        self.assertEqual(ans, expected_ans)

    def is_power_of_three(self, num):
        while num >= 3 and 0 == num % 3:
            num //= 3
        return 1 == num
