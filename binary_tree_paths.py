class Solution(object):
    def binary_tree_paths(self, root):
        self.paths = []
        self.traverse(root, [])
        return self.paths

    def traverse(self, root, cur):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.paths.append('->'.join(cur + [str(root.val)]))
        self.traverse(root.left, cur + [str(root.val)])
        self.traverse(root.right, cur + [str(root.val)])
