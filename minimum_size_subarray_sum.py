class Solution(object):
    def min_sub_array_len(self, s, nums):
        # Handle simple scenarios
        if sum(nums) < s:
            return 0
        if max(nums) >= s:
            return 1

        # Initialise min_len to the length of nums
        min_len = len(nums)
        total = left = right = 0
        while right < len(nums):
            while total < s and right < len(nums):
                total += nums[right]
                right += 1

            while total >= s:
                min_len = min(min_len, right - left)
                total -= nums[left]
                left += 1

        return min_len
