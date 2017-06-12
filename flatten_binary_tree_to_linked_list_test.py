from unittest import TestCase

from flatten_binary_tree_to_linked_list import Solution
from utils_tree import compare_trees, construct_tree, TreeNode


class TestFlattenBinaryTreeToLinkedList(TestCase):
    def test_flatten(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        sol.flatten(root)
        flattened_tree_raw = [4, 2, 1, 3, 6, 5, 7]
        expected_root = TreeNode(flattened_tree_raw[0])
        node = expected_root
        for n in flattened_tree_raw[1:]:
            node.right = TreeNode(n)
            node = node.right

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
