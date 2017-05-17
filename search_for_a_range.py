class Solution(object):
    def search_range(self, nums, target):
        if 0 == len(nums):
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        first = left
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        last = left if nums[left] == target else left - 1
        return [first, last]
