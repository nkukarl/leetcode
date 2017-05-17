class Solution(object):
    def distribute_candies(self, candies):
        return min(len(candies) // 2, len(set(candies)))
