from unittest import TestCase

from invert_binary_tree import Solution
from utils_tree import compare_trees, construct_tree


class TestInvertBinaryTree(TestCase):
    def test_invert_tree(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        root = sol.invert_tree(root)
        expected_serialized_data = [[4], [6, 2], [7, 5, 3, 1]]
        expected_root = construct_tree(expected_serialized_data)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
