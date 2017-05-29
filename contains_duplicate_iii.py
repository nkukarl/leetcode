# TODO: Should use bucket sort!
class Solution(object):
    def contains_nearby_almost_duplicate(self, nums, k, t):
        summary = {}
        for i, n in enumerate(nums):
            if len(summary) < 2 * t:
                for m in summary:
                    if abs(m - n) <= t and i - summary[m] <= k:
                        return True
            else:
                for m in range(n - t, n + t + 1):
                    if i - summary.get(m, -k - 1) <= k:
                        return True
            summary[n] = i
        return False
