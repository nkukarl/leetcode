from unittest import TestCase

from nose_parameterized import parameterized

from maximum_product_subarray import Solution


class TestMaximumProductSubarray(TestCase):
    @parameterized.expand([
        # [
        #     {
        #         'nums': [2],
        #     },
        #     2,
        # ],
        [
            {
                'nums': [2, 3, -2, 4],
            },
            6,
        ],
        [
            {
                'nums': [-1, 2, 3, 4],
            },
            24,
        ],
        [
            {
                'nums': [-1, 0, 1, -1, 0, 1],
            },
            1,
        ],
        [
            {
                'nums': [-1, 0, -1, -2, 0, 1],
            },
            2,
        ],
    ])
    def test_max_product(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_product(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
