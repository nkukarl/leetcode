class Solution(object):
    def zigzag_level_order(self, root):
        self.ans = []
        self.traverse(root, 0)
        return self.ans

    def traverse(self, root, level):
        if root is None:
            return
        if level >= len(self.ans):
            self.ans.append([])
        if 1 == level % 2:
            self.ans[level].insert(0, root.val)
        else:
            self.ans[level].append(root.val)
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
