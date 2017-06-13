class Solution(object):
    def can_jump(self, nums):
        right = 0
        for i, n in enumerate(nums):
            if i <= right:
                right = max(right, i + n)
        return right >= len(nums) - 1
