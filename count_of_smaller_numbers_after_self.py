# TODO: Anything more efficient?
class SegmentTreeNode(object):
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left = self.right = None


class Solution(object):
    def count_smaller(self, nums):
        if 0 == len(nums):
            return []
        max_, min_ = max(nums), min(nums)
        root = self.initialise_segment_tree(min_, max_)
        ans = []
        for n in nums[::-1]:
            ans.append(self.query(root, min_, n - 1))
            self.insert(root, n)
        return ans[::-1]

    def initialise_segment_tree(self, start, end):
        root = SegmentTreeNode(start, end, 0)
        if start < end:
            mid = (start + end) // 2
            root.left = self.initialise_segment_tree(start, mid)
            root.right = self.initialise_segment_tree(mid + 1, end)
        return root

    def insert(self, root, n):
        root.count += 1
        if root.start == n and root.end == n:
            return
        mid = (root.start + root.end) // 2
        if n <= mid:
            self.insert(root.left, n)
        else:
            self.insert(root.right, n)

    def query(self, root, start, end):
        if end < start:
            return 0
        if root.start == start and root.end == end:
            return root.count
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.query(root.left, start, end)
        if start > mid:
            return self.query(root.right, start, end)
        return self.query(root.left, start, mid) + \
               self.query(root.right, mid + 1, end)
