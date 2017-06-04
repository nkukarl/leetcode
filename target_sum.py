# TODO: Fix TLE
class Solution(object):
    def find_target_sum_ways(self, nums, total):
        ans = self.execute(nums)
        return ans.count(total)

    def execute(self, nums):
        if 1 == len(nums):
            return [nums[0], -nums[0]]
        m = len(nums) // 2
        left, right = self.execute(nums[:m]), self.execute(nums[m:])
        ans = []
        for n1 in left:
            for n2 in right:
                ans.append(n1 + n2)
        return ans
