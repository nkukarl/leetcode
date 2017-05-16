class Solution(object):
    def is_subtree(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if self.is_same_tree(s, t):
            return True
        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_same_tree(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.is_same_tree(s.left, t.left) and \
               self.is_same_tree(s.right, t.right)
