from unittest import TestCase

from nose_parameterized import parameterized

from factorial_trailing_zeros import Solution


class TestFactorialTrailingZeros(TestCase):
    @parameterized.expand([
        [
            {
                'n': 625,
            },
            156,
        ],
        [
            {
                'n': 5621,
            },
            1401,
        ],
    ])
    def test_trailing_zeros(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.trailing_zeros(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
