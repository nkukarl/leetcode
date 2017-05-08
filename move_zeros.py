class Solution(object):
    def move_zeros(self, nums):
        front = 1
        for i, n in enumerate(nums):
            if n != 0:
                front = max(front, i + 1)
                continue
            while front < len(nums) and 0 == nums[front]:
                front += 1
            if front >= len(nums):
                break
            nums[i], nums[front] = nums[front], nums[i]
