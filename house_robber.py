class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max([0] + nums)
        m1, m2 = nums[0], max(nums[:2])
        for n in nums[2:]:
            m1, m2 = m2, max(m1 + n, m2)
        return max(m1, m2)
