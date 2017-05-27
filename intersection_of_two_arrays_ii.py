class Solution(object):
    def intersect(self, nums1, nums2):
        summary1, summary2 = self.summarise(nums1), self.summarise(nums2)
        unique_set = set(nums1) & set(nums2)
        intersection = []
        for n in unique_set:
            count = min(summary1[n], summary2[n])
            intersection.extend([n] * count)
        return intersection

    def summarise(self, nums):
        summary = {}
        for n in nums:
            summary[n] = summary.get(n, 0) + 1
        return summary
