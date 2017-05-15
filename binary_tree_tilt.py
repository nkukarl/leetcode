class Solution(object):
    def find_tilt(self, root):
        self.tilt = 0
        self.get_sum(root)
        return self.tilt

    def get_sum(self, root):
        if root is None:
            return 0
        sum_left = self.get_sum(root.left)
        sum_right = self.get_sum(root.right)
        self.tilt += abs(sum_left - sum_right)
        return root.val + sum_left + sum_right
