from unittest import TestCase

from invert_binary_tree import Solution
from utils_tree import get_root_tree, compare_trees


class TestInvertBinaryTree(TestCase):
    def test_invert_tree(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        root = sol.invert_tree(root)
        expected_tree_raw = tree_raw[::-1]
        expected_root = get_root_tree(expected_tree_raw)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
