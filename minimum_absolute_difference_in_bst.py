class Solution(object):
    def get_minimum_difference(self, root):
        self.min_diff = 2 ** 31
        self.explore(root)
        return self.min_diff

    def explore(self, root):
        if root is None:
            return
        if root.left is not None:
            node = root.left
            while node.right is not None:
                node = node.right
            self.min_diff = min(self.min_diff, root.val - node.val)
        if root.right is not None:
            node = root.right
            while node.left is not None:
                node = node.left
            self.min_diff = min(self.min_diff, node.val - root.val)
        self.explore(root.left)
        self.explore(root.right)
