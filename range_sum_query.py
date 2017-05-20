class SegmentTreeNode(object):
    def __init__(self, start, end, sum_):
        self.start = start
        self.end = end
        self.sum_ = sum_
        self.left = self.right = None


class NumArray(object):
    def __init__(self, nums):
        start, end = 0, len(nums) - 1
        self.root = self.build(nums, start, end)

    def build(self, nums, start, end):
        if start < end:
            root = SegmentTreeNode(start, end, sum(nums[start: end + 1]))
            mid = (start + end) // 2
            root.left = self.build(nums, start, mid)
            root.right = self.build(nums, mid + 1, end)
            return root
        elif start == end:
            return SegmentTreeNode(start, end, nums[start])

    def update(self, i, val):
        if self.root is None:
            return
        current_val = self.sum_range(i, i)
        diff = val - current_val
        self._update(self.root, i, diff)

    def _update(self, root, i, diff):
        start, end = root.start, root.end
        root.sum_ += diff
        if root.start == root.end:
            return
        mid = (start + end) // 2
        if i <= mid:
            self._update(root.left, i, diff)
        else:
            self._update(root.right, i, diff)

    def sum_range(self, i, j):
        if self.root is None:
            return 0
        i, j = min(i, j), max(i, j)
        root = self.root
        start, end = max(root.start, i), min(root.end, j)
        return self._sum_range(root, start, end)

    def _sum_range(self, root, start, end):
        if root.start == start and root.end == end:
            return root.sum_
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self._sum_range(root.left, start, end)
        if start > mid:
            return self._sum_range(root.right, start, end)
        return self._sum_range(root.left, start, mid) + \
               self._sum_range(root.right, mid + 1, end)
