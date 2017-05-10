class Solution(object):
    def convert_bst(self, root):
        self.current = 0
        self._convert(root)
        return root

    def _convert(self, root):
        if root is None:
            return
        self._convert(root.right)
        self.current += root.val
        root.val = self.current
        self._convert(root.left)
