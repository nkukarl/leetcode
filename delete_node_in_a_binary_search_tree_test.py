from unittest import TestCase

from nose_parameterized import parameterized

from delete_node_in_a_binary_search_tree import Solution
from utils_tree import compare_trees, get_root_tree, TreeNode


class TestDeleteNodeInABinarySearchTree(TestCase):
    @parameterized.expand([
        [
            [1, 2, 3, 4, 5, 6, 7],
            1,
            [None, 2, 3, 4, 5, 6, 7]
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            2,
            [None, 1, 3, 4, 5, 6, 7]
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            3,
            [1, 2, None, 4, 5, 6, 7]
        ],
    ])
    def test_delete_node_simple(self, tree_raw, key_, expected_tree_raw):
        # Setup
        sol = Solution()
        root = get_root_tree(tree_raw)

        # Exercise
        root = sol.delete_node(root, key_)

        # Verify
        expected_root = get_root_tree(expected_tree_raw)
        self.assertTrue(compare_trees(root, expected_root))

    def test_delete_node_complicated(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)
        key_ = 4

        # Exercise
        root = sol.delete_node(root, key_)

        # Verify
        expected_root = TreeNode(2)
        expected_root.left = TreeNode(1)
        expected_root.right = TreeNode(3)
        expected_root.right.right = TreeNode(6)
        expected_root.right.right.left = TreeNode(5)
        expected_root.right.right.right = TreeNode(7)
        self.assertTrue(compare_trees(root, expected_root))
