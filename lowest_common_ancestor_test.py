import random
from unittest import TestCase

from lowest_common_ancestor import Solution
from utils_tree import compare_trees, construct_tree


class TestLowestCommonAncestorOfABinarySearchTree(TestCase):
    def test_lowest_common_ancestor_bst(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)
        p, q = root.left.left, root.left.right

        # Exercise
        lca = sol.lowest_common_ancestor_bst(root, p, q)
        expected_lca = self.lowest_common_ancestor_bst(root, p, q)

        # Verify
        self.assertTrue(compare_trees(lca, expected_lca))

    def lowest_common_ancestor_bst(self, root, p, q):
        """

        Iterative solution

        Args:
            root (TreeNode):
            p (TreeNode):
            q (TreeNode):

        Returns:

        """
        while True:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

    def test_lowest_common_ancestor(self):
        # Setup
        sol = Solution()
        serialized_data_raw = [1, 2, 3, 4, 5, 6, 7]
        random.shuffle(serialized_data_raw)
        serialized_data = [
            serialized_data_raw[:1],
            serialized_data_raw[1:3],
            serialized_data_raw[3:],
        ]
        root = construct_tree(serialized_data)
        p, q = root.left.left, root.left.right

        # Exercise
        lca = sol.lowest_common_ancestor(root, p, q)
        expected_lca = self.lowest_common_ancestor(root, p, q)

        # Verify
        self.assertTrue(compare_trees(lca, expected_lca))

    def lowest_common_ancestor(self, root, p, q):
        if p is None:
            return q
        if q is None:
            return p
        if self.is_subtree(root.left, p) and self.is_subtree(root.left, q):
            return self.lowest_common_ancestor(root.left, p, q)
        if self.is_subtree(root.right, p) and self.is_subtree(root.right, q):
            return self.lowest_common_ancestor(root.right, p, q)
        return root

    def is_subtree(self, root, node):
        if node is None:
            return True
        if root is None:
            return False
        if node == root:
            return True
        return self.is_subtree(root.left, node) or \
               self.is_subtree(root.right, node)
