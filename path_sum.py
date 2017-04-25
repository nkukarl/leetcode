class Solution(object):
    def has_path_sum(self, root, sum_):
        self.sum_ = sum_
        self.flag = False
        self.traverse_flag(root, 0)
        return self.flag

    def traverse_flag(self, root, cur):
        if root is None:
            return
        if root.left is None and root.right is None:
            if cur + root.val == self.sum_:
                self.flag = True
        self.traverse_flag(root.left, cur + root.val)
        self.traverse_flag(root.right, cur + root.val)

    def path_sum(self, root, sum_):
        self.sum_ = sum_
        self.valid_paths = []
        self.traverse_path(root, [])
        return self.valid_paths

    def traverse_path(self, root, cur):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum(cur) + root.val == self.sum_:
                self.valid_paths.append(cur + [root.val])
        self.traverse_path(root.left, cur + [root.val])
        self.traverse_path(root.right, cur + [root.val])
