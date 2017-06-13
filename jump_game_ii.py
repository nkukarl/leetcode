class Solution(object):
    def jump(self, nums):
        # Handle simple scenario
        if 1 == len(nums):
            return 0
        # Handle general scenario
        left, right = 0, nums[0]
        cur = 0
        step = 1
        while right < len(nums) - 1:
            step += 1
            for pos in range(left, right + 1):
                cur = max(cur, pos + nums[pos])
            left = right
            right = cur

        return step
