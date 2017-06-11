class Solution(object):
    def find_tilt(self, root):
        return self.get_tilt_and_sum(root)[0]

    def get_tilt_and_sum(self, root):
        if root is None:
            return 0, 0
        left_tilt, left_sum = self.get_tilt_and_sum(root.left)
        right_tilt, right_sum = self.get_tilt_and_sum(root.right)
        current_tilt = abs(left_sum - right_sum)

        total_tilt = left_tilt + right_tilt + current_tilt
        total_sum = left_sum + right_sum + root.val
        return total_tilt, total_sum
