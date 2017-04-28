class Solution(object):
    def check_subarray_sum(self, nums, k):
        # Handle simple scenarios
        if len(nums) < 2:
            return False
        if 0 == k:
            return 0 == sum(nums)
        if 1 == k:
            return True
        # Handle general scenarios
        current = 0
        cache = {0: -1}
        for i, num in enumerate(nums):
            current += num % k
            current %= k
            if current in cache:
                if i - cache[current] >= 2:
                    return True
            else:
                cache[current] = i
        return False
