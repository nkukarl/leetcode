class Solution(object):
    def invert_tree(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
