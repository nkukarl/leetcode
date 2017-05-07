class Solution(object):
    def maximise_profit(self, prices):
        # Handle simple scenarios
        if len(prices) < 2:
            return 0
        profits = [p2 - p1 for p2, p1 in zip(prices[1:], prices[:-1])]
        # Price keeps decreasing
        if max(profits) <= 0:
            return 0
        # Price keeps increasing
        if min(profits) >= 0:
            return sum(profits)

        max_profit = 0
        cur_profit = 0
        for p in profits:
            cur_profit += p
            if cur_profit < 0:
                cur_profit = 0
            else:
                max_profit = max(max_profit, cur_profit)
        return max_profit
