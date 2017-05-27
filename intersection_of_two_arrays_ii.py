# TODO: Follow up question
# 1. What if the given array is already sorted?
#    How would you optimize your algorithm?
# 2. What if nums1's size is small compared to nums2's size?
#    Which algorithm is better?
# 3. What if elements of nums2 are stored on disk, and the memory is limited
#    such that you cannot load all elements into the memory at once?
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
