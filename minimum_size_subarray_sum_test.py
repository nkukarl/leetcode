from unittest import TestCase

from minimum_size_subarray_sum import Solution


class TestMinimumSizeSubarraySum(TestCase):
    def test_min_sub_array_len(self):
        # Setup
        sol = Solution()
        s = 7
        nums = [2, 3, 1, 2, 4, 3]

        # Exercise
        ans = sol.min_sub_array_len(s, nums)

        # Verify
        expected_ans = 2
        self.assertEqual(ans, expected_ans)
