"""
Given a binary array, find the maximum length of
a contiguous subarray with equal number of 0 and 1.

    E.g.,
    nums = [1, 0, 1, 0, 1, 0, 1]
    Return 6 since [1, 0, 1, 0, 1, 0] is the longest
    contiguous subarray.
"""
class Solution(object):
    def find_max_length(self, nums):
        summary = self.summarise(nums)
        max_length = 0
        cache = {0: -1}
        for i, v in enumerate(summary):
            if v not in cache:
                cache[v] = i
            else:
                max_length = max(i - cache[v], max_length)
        return max_length

    def summarise(self, nums):
        summary = []
        count = 0
        for n in nums:
            if 1 == n:
                count += 1
                summary.append(count)
            else:
                count -= 1
                summary.append(count)
        return summary



