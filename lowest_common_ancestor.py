class Solution(object):
    def lowest_common_ancestor_bst(self, root, p, q):
        """

        Recursive solution

        Args:
            root (TreeNode):
            p (TreeNode):
            q (TreeNode):

        Returns:
            lowest common ancestor (TreeNode)

        """
        if root in [None, p, q]:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor_bst(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor_bst(root.right, p, q)
        return root

    def lowest_common_ancestor(self, root, p, q):
        if root in [None, p, q]:
            return root
        lca_left = self.lowest_common_ancestor(root.left, p, q)
        lca_right = self.lowest_common_ancestor(root.right, p, q)
        if lca_left is not None and lca_right is not None:
            return root
        return lca_left or lca_right
