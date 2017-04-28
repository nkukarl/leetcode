from unittest import TestCase

from nose_parameterized import parameterized

from next_permutation import Solution


class TestNextPermutation(TestCase):
    @parameterized.expand([
        [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
        ],
        [
            [4, 3, 2, 1],
            [1, 2, 3, 4],
        ],
        [
            [1, 1, 1, 5],
            [1, 1, 5, 1],
        ],
        [
            [6, 1, 5, 4, 3, 2],
            [6, 2, 1, 3, 4, 5],
        ],
        [
            [2, 4, 3, 2],
            [3, 2, 2, 4],
        ]
    ])
    def test_next_permutation(self, nums, expected_nums):
        # Setup
        sol = Solution()

        # Exercise
        sol.next_permutation(nums)

        # Verify
        self.assertEqual(nums, expected_nums)
