class Solution(object):
    def max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
