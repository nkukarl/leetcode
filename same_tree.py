class Solution(object):
    def is_same_tree(self, root1, root2):
        if root1 is not None and root2 is not None:
            return root1.val == root2.val and \
                   self.is_same_tree(root1.left, root2.left) and \
                   self.is_same_tree(root1.right, root2.right)
        return root1 == root2
