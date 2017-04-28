class Solution(object):
    def next_permutation(self, nums):
        index = len(nums) - 1
        pivot = None
        while index > 0:
            # To get previous permutation, change '<' to '>'
            if nums[index - 1] < nums[index]:
                pivot = index - 1
                break
            index -= 1
        if pivot is None:
            nums.reverse()
            return
        index = len(nums) - 1
        while True:
            # To get previous permutation, change '<' to '>'
            if nums[pivot] < nums[index]:
                break
            index -= 1
        nums[pivot], nums[index] = nums[index], nums[pivot]
        self.partial_reverse(nums, pivot + 1, len(nums) - 1)

    def partial_reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
