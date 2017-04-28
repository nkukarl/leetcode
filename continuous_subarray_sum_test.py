import random
from unittest import TestCase

from nose_parameterized import parameterized

from continuous_subarray_sum import Solution


class TestContinuousSubarraySum(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1],
                'k': random.randint(1, 100),
            },
            False,
        ],
        [
            {
                'nums': [1, 2],
                'k': 0,
            },
            False,
        ],
        [
            {
                'nums': [0, 0, 0],
                'k': 0,
            },
            True,
        ],
        [
            {
                'nums': [0, 0, 0],
                'k': 1,
            },
            True,
        ],
        [
            {
                'nums': [23, 2, 4, 6, 7],
                'k': 6,
            },
            True,
        ],
        [
            {
                'nums': [23, 2, 6, 4, 7],
                'k': 7,
            },
            True,
        ],
    ])
    def test_check_subarray_sum(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.check_subarray_sum(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
