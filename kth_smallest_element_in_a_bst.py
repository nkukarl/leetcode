class Solution(object):
    def kth_smallest(self, root, k):
        self.k = k
        self.count = 0
        self.ans = None
        self.traverse(root)
        return self.ans

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.count += 1
        if self.count == self.k:
            self.ans = root.val
            return
        self.traverse(root.right)
