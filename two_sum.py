class Solution:
    def two_sum(self, nums, target):
        cache = dict()
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in cache:
                return cache[new_target], i
            cache[nums[i]] = i

    def two_sum_sorted_nums(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ == target:
                return left, right
            if sum_ < target:
                left += 1
            else:
                right -= 1
