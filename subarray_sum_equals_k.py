class Solution(object):
    def subarray_sum(self, nums, k):
        ans = total = 0
        summary = {0: 1}
        for n in nums:
            total += n
            ans += summary.get(total - k, 0)
            summary[total] = summary.get(total, 0) + 1
        return ans
