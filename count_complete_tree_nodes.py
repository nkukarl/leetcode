class Solution(object):
    def count_nodes(self, root):
        if root is None:
            return 0
        depth_left = self.get_depth(root.left)
        depth_right = self.get_depth(root.right)
        if depth_left == depth_right:
            return 2 ** depth_left + self.count_nodes(root.right)
        return 2 ** depth_right + self.count_nodes(root.left)

    def get_depth(self, root):
        if root is None:
            return 0
        return 1 + self.get_depth(root.left)
