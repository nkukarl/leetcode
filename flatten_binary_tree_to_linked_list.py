class Solution(object):
    def flatten(self, root):
        self._flatten(root)

    def _flatten(self, root):
        if root is None:
            return
        # Flatten right branch
        root.right = self._flatten(root.right)
        # Flatten left branch if it exists
        if root.left is not None:
            flattened_left = self._flatten(root.left)
            # Cut left branch
            root.left = None
            # If right branch does not exist, add flattened left branch
            if root.right is None:
                root.right = flattened_left
            # Otherwise, insert flattened left branch
            else:
                flattened_right = root.right
                root.right = flattened_left
                last = self.get_last(flattened_left)
                last.right = flattened_right
        return root

    def get_last(self, root):
        last = root
        while root.right is not None:
            root = root.right
            last = root
        return last
