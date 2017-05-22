class Solution(object):
    def coin_change(self, coins, amount):
        coins.sort()
        counts = [0] + [amount + 1] * amount
        for coin in coins:
            for a in range(coin, amount + 1):
                counts[a] = min(counts[a], counts[a - coin] + 1)
        return counts[-1] if counts[-1] <= amount else -1
