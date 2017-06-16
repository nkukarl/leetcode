from unittest import TestCase

from nose_parameterized import parameterized

from find_minimum_in_rotated_sorted_array import Solution


class TestFindMinimumInRotatedSortedArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 2, 3, 4, 5, 6, 7],
            },
        ],
        [
            {
                'nums': [2, 3, 4, 5, 6, 7, 1],
            },
        ],
        [
            {
                'nums': [3, 4, 5, 6, 7, 1, 2],
            },
        ],
        [
            {
                'nums': [4, 5, 6, 7, 1, 2, 3],
            },
        ],
        [
            {
                'nums': [5, 6, 7, 1, 2, 3, 4],
            },
        ],
        [
            {
                'nums': [6, 7, 1, 2, 3, 4, 5],
            },
        ],
        [
            {
                'nums': [7, 1, 2, 3, 4, 5, 6],
            },
        ],
    ])
    def test_find_min(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_min(**kwargs)

        # Verify
        expected_ans = self.find_min(**kwargs)
        self.assertEqual(ans, expected_ans)

    def find_min(self, nums):
        return min(nums)
