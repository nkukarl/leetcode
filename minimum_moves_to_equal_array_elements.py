class Solution(object):
    def min_moves(self, nums):
        if 0 == len(nums):
            return 0
        return sum(nums) - len(nums) * min(nums)
