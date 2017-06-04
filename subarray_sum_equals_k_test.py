from unittest import TestCase

from nose_parameterized import parameterized

from subarray_sum_equals_k import Solution


class TestSubarraySumEqualsK(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 1],
                'k': 2,
            },
            2,
        ],
    ])
    def test_subarray_sum(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.subarray_sum(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
