class Solution(object):
    def next_permutation(self, nums):
        index = len(nums) - 2
        pivot = None
        while index > -1:
            if nums[index] < nums[index + 1]:
                pivot = index
                break
            index -= 1
        if pivot is None:
            nums.reverse()
            return
        index = len(nums) - 1
        while True:
            if nums[index] > nums[pivot]:
                break
            index -= 1
        nums[pivot], nums[index] = nums[index], nums[pivot]
        self.partial_reverse(nums, pivot + 1, len(nums) - 1)

    def partial_reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
