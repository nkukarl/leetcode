class Solution(object):
    def find_pairs(self, nums, k):
        if k < 0:
            return 0
        summary = {}
        for i, n in enumerate(nums):
            summary[n] = summary.get(n, []) + [i]
        pairs = set()
        for val, ind in summary.items():
            if 0 == k:
                if len(ind) > 1:
                    pairs.add((val, val))
                continue
            ind1 = summary.get(val - k, [])
            if len(ind1) > 0:
                pairs.add((min(val, val - k), max(val, val - k)))
            ind2 = summary.get(val + k, [])
            if len(ind2) > 0:
                pairs.add((min(val, val + k), max(val, val + k)))
        return len(pairs)
