from unittest import TestCase

from nose_parameterized import parameterized

from partition_equal_subset_sum import Solution


class TestPartitionEqualSubsetSum(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 5, 11, 5],
            },
            True,
        ],
        [
            {
                'nums': [1, 2, 3, 5],
            },
            False,
        ],
    ])
    def test_can_partition(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.can_partition(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
