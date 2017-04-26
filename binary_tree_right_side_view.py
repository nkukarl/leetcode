class Solution(object):
    def right_side_view(self, root):
        self.node_vals = []
        self.traverse(root, 0)
        return [level_vals[-1] for level_vals in self.node_vals]

    def traverse(self, root, level):
        if root is None:
            return
        if level >= len(self.node_vals):
            self.node_vals.append([])
        self.node_vals[level].append(root.val)
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
