from unittest import TestCase

from nose_parameterized import parameterized

from best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(TestCase):
    @parameterized.expand([
        [
            {
                'prices': [7, 1, 5, 3, 6, 4],
            },
            5,
        ],
        [
            {
                'prices': [7, 6, 4, 3, 1],
            },
            0,
        ],
    ])
    def test_maximise_profit(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.maximise_profit(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
