from unittest import TestCase
from two_sum import Solution


class TestTwoSum(TestCase):
    def test_twoSum(self):
        # Setup
        sol = Solution()
        numbers = [2, 7, 11, 15]
        target = 17

        # Exercise
        ans = sol.two_sum(numbers, target)

        # Verify
        self.assertEqual(ans, [0, 3])
