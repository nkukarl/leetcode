class Solution(object):
    def diameter_of_binary_tree(self, root):
        self.diameter = 0
        self.get_depth(root)
        return self.diameter

    def get_depth(self, root):
        if root is None:
            return 0
        depth_left = self.get_depth(root.left)
        depth_right = self.get_depth(root.right)
        self.diameter = max(self.diameter, depth_left + depth_right)
        return 1 + max(depth_left, depth_right)
