from unittest import TestCase

from nose_parameterized import parameterized

from three_sum import Solution


class TestThreeSum(TestCase):
    @parameterized.expand([
        [
            {
                'numbers': [-1, 0, 1, 2, -1, 4],
                'target': 0,
            },
            [
                [-1, -1, 2],
                [-1, 0, 1],
            ]
        ],
        [
            {
                'numbers': [0] * 1000,
                'target': 0,
            },
            [
                [0, 0, 0],
            ]
        ],
    ])
    def test_three_Sum(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.three_sum(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
