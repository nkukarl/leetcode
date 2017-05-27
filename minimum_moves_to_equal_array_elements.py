class Solution(object):
    def min_moves(self, nums):
        if 0 == len(nums):
            return 0
        return sum(nums) - len(nums) * min(nums)

    def min_moves2(self, nums):
        if 0 == len(nums):
            return 0
        nums.sort()
        median = nums[len(nums) // 2]
        return sum([abs(n - median) for n in nums])
