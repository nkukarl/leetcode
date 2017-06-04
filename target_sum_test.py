from unittest import TestCase

from nose_parameterized import parameterized

from target_sum import Solution


class TestTargetSum(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 1, 1, 1],
                'total': 3,
            },
            5,
        ],
        [
            {
                'nums': [1, 1, 1, 1, 1],
                'total': 4,
            },
            0,
        ],
        [
            {
                'nums': [
                    44, 20, 38, 6, 2, 47, 18, 50, 41, 38, 32, 24, 38, 38, 30, 5,
                    26, 15, 37, 35,
                ],
                'total': 44,
            },
            4983,
        ]
    ])
    def test_find_target_sum_ways(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_target_sum_ways(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
