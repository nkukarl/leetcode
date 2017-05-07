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

        l2r_profits = self.get_current_max_profit(profits)
        r2l_profits = self.get_current_max_profit(profits[::-1])[::-1]

        return max([p1 + p2 for p1, p2 in zip(l2r_profits, r2l_profits)])

    def get_current_max_profit(self, profits):
        max_profits = [0]
        max_profit = cur_profit = 0
        for p in profits:
            cur_profit += p
            if cur_profit < 0:
                cur_profit = 0
            max_profit = max(max_profit, cur_profit)
            max_profits.append(max_profit)
        return max_profits
