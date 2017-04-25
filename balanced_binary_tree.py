class Solution(object):
    def is_balanced(self, root):
        if root is None:
            return True
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def get_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))
