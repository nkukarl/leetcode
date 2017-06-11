class Solution(object):
    def move_zeros(self, nums):
        m = len(nums)

        # Find the index of the first zero
        slow = 0
        while slow < m and nums[slow] != 0:
            slow += 1

        # If slow has reached te end of nums, simply return.
        if slow >= m - 1:
            return

        # Find the index of the first non-zero after the first zero
        fast = slow + 1
        while fast < m:
            while fast < m and 0 == nums[fast]:
                fast += 1
            if fast < m:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
