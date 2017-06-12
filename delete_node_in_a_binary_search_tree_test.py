from unittest import TestCase

from nose_parameterized import parameterized

from delete_node_in_a_binary_search_tree import Solution
from utils_tree import compare_trees, construct_tree, TreeNode


class TestDeleteNodeInABinarySearchTree(TestCase):
    @parameterized.expand([
        [
            [[4], [2, 6], [1, 3, 5, 7]],
            1,
            [[4], [2, 6], [None, 3, 5, 7]],
        ],
        [
            [[4], [2, 6], [1, 3, 5, 7]],
            2,
            [[4], [1, 6], [None, 3, 5, 7]],
        ],
        [
            [[4], [2, 6], [1, 3, 5, 7]],
            3,
            [[4], [2, 6], [1, None, 5, 7]],
        ],
    ])
    def test_delete_node_simple(self, serialized_data, key_,
                                expected_serialized_data):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        root = sol.delete_node(root, key_)

        # Verify
        expected_root = construct_tree(expected_serialized_data)
        self.assertTrue(compare_trees(root, expected_root))

    def test_delete_node_complicated(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)
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
