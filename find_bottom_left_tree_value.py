class Solution(object):
    def find_bottom_left_value(self, root):
        self.node_values = []
        self.traverse(root, 0)
        return self.node_values[-1][0]

    def traverse(self, root, level):
        if root is None:
            return
        if level >= len(self.node_values):
            self.node_values.append([])
        self.node_values[level].append(root.val)
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
