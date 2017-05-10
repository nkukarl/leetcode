from unittest import TestCase

from convert_bst_to_greater_tree import Solution
from utils_tree import compare_trees, get_root_tree


class TestConvertBSTToGreaterTree(TestCase):
    def test_convert_bst(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        root = sol.convert_bst(root)

        # Verify
        expected_tree_raw = [28, 27, 25, 22, 18, 13, 7]
        expected_root = get_root_tree(expected_tree_raw)
        self.assertTrue(compare_trees(root, expected_root))
