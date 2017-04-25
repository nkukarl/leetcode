class Solution(object):
    def binary_tree_paths(self, root):
        self.paths = []
        self.traverse(root, [])
        return self.paths

    def traverse(self, root, cur):
        if root is None:
            return
        next_ = cur + [str(root.val)]
        if root.left is None and root.right is None:
            self.paths.append('->'.join(next_))
        self.traverse(root.left, next_)
        self.traverse(root.right, next_)
