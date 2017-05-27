from unittest import TestCase

from nose_parameterized import parameterized

from product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [],
            },
            [],
        ],
        [
            {
                'nums': [1, 2, 3, 4],
            },
            [24, 12, 8, 6],
        ],
        [
            {
                'nums': [1, 3, 5, 0, 3, 0],
            },
            [0, 0, 0, 0, 0, 0],
        ],
        [
            {
                'nums': [1, 3, 5, 0, 3, 1],
            },
            [0, 0, 0, 45, 0, 0],
        ],
    ])
    def test_product_except_self(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.product_except_self(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
