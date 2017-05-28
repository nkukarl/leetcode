from unittest import TestCase

from nose_parameterized import parameterized

from range_addition_ii import Solution


class TestRangeAdditionII(TestCase):
    @parameterized.expand([
        [
            {
                'm': 10,
                'n': 15,
                'ops': [
                    [3, 4], [7, 5], [2, 2], [9, 10],
                ],
            },
            4,
        ],
    ])
    def test_max_count(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_count(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
