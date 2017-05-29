class Solution(object):
    def contains_nearby_duplicate(self, nums, k):
        summary = {}
        for i, n in enumerate(nums):
            if n not in summary:
                summary[n] = i
            else:
                if i - summary[n] <= k:
                    return True
                summary[n] = i
        return False
