class Solution(object):
    def remove_duplicates(self, nums):
        N = len(nums)
        if N < 2:
            return N
        front = 2
        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                while front < N and nums[front] <= nums[i - 1]:
                    front += 1
                if front >= N:
                    return i
                nums[i], nums[front] = nums[front], nums[i]
        return N
