class Solution(object):
    def is_valid_bst(self, root):
        return self.validate(root, -2 ** 31 - 1, 2 ** 31 + 1)

    def validate(self, root, low, high):
        if root is None:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.validate(root.left, low, root.val) and \
               self.validate(root.right, root.val, high)
