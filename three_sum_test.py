from unittest import TestCase

from three_sum import Solution


class TestThreeSum(TestCase):
    def test_three_Sum(self):
        # Setup
        sol = Solution()
        numbers = [-1, 0, 1, 2, -1, 4]
        target = 0

        # Exercise
        ans = sol.three_sum(numbers, target)

        # Verify
        self.assertEqual(
            ans,
            [[-1, -1, 2], [-1, 0, 1]]
        )
