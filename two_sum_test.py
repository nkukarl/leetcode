from unittest import TestCase

from two_sum import Solution


class TestTwoSum(TestCase):
    def test_two_sum(self):
        # Setup
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 17

        # Exercise
        ans = sol.two_sum(nums, target)

        # Verify
        self.assertEqual(ans, (0, 3))

    def test_two_sum_sorted_nums(self):
        # Setup
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9

        # Exercise
        ans = sol.two_sum_sorted_nums(nums, target)

        # Verify
        self.assertEqual(ans, (0, 1))
