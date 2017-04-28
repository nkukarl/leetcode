class Solution(object):
    def largest_values(self, root):
        self.largest = []
        self.get_largest(root, 0)
        return self.largest

    def get_largest(self, root, level):
        if root is None:
            return
        if level >= len(self.largest):
            self.largest.append(root.val)
        else:
            self.largest[level] = max(self.largest[level], root.val)
        self.get_largest(root.left, level + 1)
        self.get_largest(root.right, level + 1)
