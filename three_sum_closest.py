class Solution(object):
    def three_sum_closest(self, nums, target):
        if len(nums) < 3:
            return None
        nums.sort()
        closest = sum(nums[:3])
        diff_min = abs(closest - target)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ = sum([nums[i], nums[j], nums[k]])
                if sum_ == target:
                    return target
                if sum_ < target:
                    j += 1
                else:
                    k -= 1
                diff = abs(target - sum_)
                if diff < diff_min:
                    diff_min = diff
                    closest = sum_
        return closest
