class Solution(object):
    def combine(self, n, k):
        # Get available numbers
        nums = [x for x in range(1, n + 1)]
        # Handle simple scenarios
        if 0 == k:
            return [[]]
        if n == k:
            return [nums]
        # Handle general scenarios
        self.ans = []
        if k <= n // 2:
            self.exercise(nums, [], k)
            return self.ans
        # If k is greater than half of n, exercise for n - k
        # to save time
        self.exercise(nums, [], n - k)
        return [list(set(nums) - set(ar)) for ar in self.ans]

    def exercise(self, nums, cur, k):
        if len(cur) == k:
            self.ans.append(cur)
        else:
            for i, num in enumerate(nums):
                self.exercise(nums[i + 1:], cur + [num], k)
