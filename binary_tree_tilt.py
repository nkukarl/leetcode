class Solution(object):
    def find_tilt(self, root):
        self.tilt = 0
        self.explore(root)
        return self.tilt

    def explore(self, root):
        if root is None:
            return 0
        sum_left = self.explore(root.left)
        sum_right = self.explore(root.right)
        self.tilt += abs(sum_left - sum_right)
        return root.val + sum_left + sum_right
