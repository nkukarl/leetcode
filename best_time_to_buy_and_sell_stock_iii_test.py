from unittest import TestCase

from nose_parameterized import parameterized

from best_time_to_buy_and_sell_stock_iii import Solution


class TestBestTimeToBuyAndSellStockIII(TestCase):
    @parameterized.expand([
        [
            {
                'prices': [1, 3, 2, 5, 0, 1, 2, 4],
            },
            8,
        ],
    ])
    def test_maximise_profit(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.maximise_profit(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
