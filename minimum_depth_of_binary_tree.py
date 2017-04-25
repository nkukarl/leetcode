class Solution(object):
    def min_depth(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.min_depth(root.right)
        if root.right is None:
            return 1 + self.min_depth(root.left)
        return 1 + min(self.min_depth(root.left), self.min_depth(root.right))

    def get_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))
