class Solution(object):
    def max_product(self, nums):
        max_ = cur_max = cur_min = nums[0]
        for n in nums[1:]:
            new_max = max(n, cur_max * n, cur_min * n)
            new_min = min(n, cur_max * n, cur_min * n)
            cur_max, cur_min = new_max, new_min
            max_ = max(cur_max, max_)
        return max_
