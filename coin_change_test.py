from unittest import TestCase

from nose_parameterized import parameterized

from coin_change import Solution


class TestCoinChange(TestCase):
    @parameterized.expand([
        [
            {
                'coins': [1, 2, 5],
                'amount': 11,
            },
            3,
        ],
        [
            {
                'coins': [2],
                'amount': 3,
            },
            -1,
        ],
        [
            {
                'coins': [1],
                'amount': 0,
            },
            0,
        ]
    ])
    def test_coin_change(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.coin_change(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
