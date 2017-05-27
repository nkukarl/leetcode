# TODO: Fix TLE
class Solution(object):
    def can_partition(self, nums):
        if 0 == len(nums):
            return True
        sum_ = sum(nums)
        if 1 == sum_ % 2:
            return False
        total = sum_ // 2
        return self.can_get_subset(nums, total)

    def can_get_subset(self, nums, total):
        self.total = total
        return self.explore(nums, 0)

    def explore(self, nums, total):
        if total == self.total:
            return True
        if total > self.total:
            return False
        for i, n in enumerate(nums):
            if self.explore(nums[:i] + nums[i + 1:], total + n):
                return True
        return False
