from unittest import TestCase

from nose_parameterized import parameterized

from subsets import Solution


class TestSubsets(TestCase):
    @parameterized.expand([
        [
            [1, 2, 3],
            [
                [],
                [1], [2], [3],
                [1, 2], [1, 3], [2, 3],
                [1, 2, 3],
            ]
        ],
        [
            [1, 2],
            [
                [],
                [1], [2],
                [1, 2],
            ]
        ],
    ])
    def test_subsets(self, nums, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.subsets(nums)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
