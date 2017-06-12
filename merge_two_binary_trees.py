class Solution(object):
    def merge_trees(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 or t2
        t1.left = self.merge_trees(t1.left, t2.left)
        t1.right = self.merge_trees(t1.right, t2.right)
        t1.val += t2.val
        return t1
