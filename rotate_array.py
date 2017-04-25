class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n <= 1:
            return
        k %= n
        if 0 == k:
            return
        m = n - k
        self._reverse(nums, 0, m - 1)
        self._reverse(nums, m, n - 1)
        self._reverse(nums, 0, n - 1)

    def _reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
