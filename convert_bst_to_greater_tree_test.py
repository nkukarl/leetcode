from unittest import TestCase

from convert_bst_to_greater_tree import Solution
from utils_tree import compare_trees, construct_tree


class TestConvertBSTToGreaterTree(TestCase):
    def test_convert_bst(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        root = sol.convert_bst(root)

        # Verify
        expected_tree_raw = [[22], [27, 13], [28, 25, 18, 7]]
        expected_root = construct_tree(expected_tree_raw)
        self.assertTrue(compare_trees(root, expected_root))
