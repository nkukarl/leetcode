from unittest import TestCase
from two_sum import Solution


class TestTwoSum(TestCase):
    def test_twoSum(self):
        sol = Solution()

        numbers = [2, 7, 11, 15]
        target = 17

        ans = sol.two_sum(numbers, target)

        self.assertEqual(ans, [0, 3])
