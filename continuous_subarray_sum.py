class Solution(object):
    def check_subarray_sum(self, nums, k):
        """
        
        Args:
            nums: A list of non-negative numbers 
            k: A target integer

        Returns:
            bool

        """
        if 0 == k:
            # This ensures cur + n does not change when mod by k
            # which is equivalent to
            # cur = (cur + n) % k if k else (cur + n)
            # Using abs to ensure that it also works when negatives numbers
            # exist in nums.
            k = sum(map(abs, nums)) + 1
        cur = 0
        cache = {0: -1}
        for i, n in enumerate(nums):
            cur = (cur + n) % k
            if cur not in cache:
                cache[cur] = i
            elif i - cache[cur] > 1:
                return True

        return False
