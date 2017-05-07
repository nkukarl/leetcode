class Solution(object):
    def find_disappeared_numbers(self, nums):
        for n in nums:
            m = abs(n)
            nums[m - 1] = -abs(nums[m - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]
