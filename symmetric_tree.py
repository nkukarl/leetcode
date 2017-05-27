class Solution(object):
    def is_symmetric(self, root):
        if root is None:
            return True
        return self._is_symm(root.left, root.right)

    def _is_symm(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if None in [root1, root2]:
            return False
        if root1.val != root2.val:
            return False
        return self._is_symm(root1.left, root2.right) and \
               self._is_symm(root1.right, root2.left)
