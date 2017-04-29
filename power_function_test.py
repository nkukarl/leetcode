from unittest import TestCase

from nose_parameterized import parameterized

from power_function import Solution


class TestPowerFunction(TestCase):
    @parameterized.expand([
        [
            {
                'x': 3.0,
                'n': 5,
            },
        ],
        [
            {
                'x': 1.0,
                'n': 5,
            },
        ],
        [
            {
                'x': 2.0,
                'n': -4,
            },
        ],
        [
            {
                'x': 2.0,
                'n': -2147483648,
            }
        ]
    ])
    def test_power_function(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.power_function(**kwargs)
        expected_ans = kwargs['x'] ** kwargs['n']

        # Verify
        self.assertEqual(ans, expected_ans)
