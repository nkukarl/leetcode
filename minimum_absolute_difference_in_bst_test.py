import random
from unittest import TestCase

from minimum_absolute_difference_in_bst import Solution
from utils_tree import get_root_tree


class TestMinimumAbsoluteDifferenceInBST(TestCase):
    def test_get_minimum_difference(self):
        # Setup
        sol = Solution()
        tree_raw = sorted(random.sample(list(range(1000)), 7))
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.get_minimum_difference(root)

        # Verify
        expected_ans = self.get_minimum_difference(root)
        self.assertEqual(ans, expected_ans)

    def test_get_minimum_difference_inorder_traverse(self):
        # Setup
        sol = Solution()
        tree_raw = sorted(random.sample(list(range(1000)), 7))
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.get_minimum_difference_inorder_traverse(root)

        # Verify
        expected_ans = self.get_minimum_difference(root)
        self.assertEqual(ans, expected_ans)

    def get_minimum_difference(self, root):
        self.min_diff = 2 ** 31
        self.explore(root)
        return self.min_diff

    def explore(self, root):
        if root is None:
            return
        if root.left is not None:
            node = root.left
            while node.right is not None:
                node = node.right
            self.min_diff = min(self.min_diff, root.val - node.val)
        if root.right is not None:
            node = root.right
            while node.left is not None:
                node = node.left
            self.min_diff = min(self.min_diff, node.val - root.val)
        self.explore(root.left)
        self.explore(root.right)
