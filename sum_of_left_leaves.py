class Solution(object):
    def sum_of_left_leaves(self, root):
        self.total = 0
        self.explore(root, False)
        return self.total

    def explore(self, root, is_left):
        if root is None:
            return
        if root.left is None and root.right is None:
            if is_left:
                self.total += root.val
        else:
            self.explore(root.left, True)
            self.explore(root.right, False)
