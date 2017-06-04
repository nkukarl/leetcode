from unittest import TestCase

from utils_tree import construct_tree, compare_trees, TreeNode


class TestConstructTree(TestCase):
    def test_complete_tree(self):
        # Setup
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]

        # Exercise
        root = construct_tree(serialized_data)

        # Verify
        expected_root = TreeNode(4)
        expected_root.left = TreeNode(2)
        expected_root.right = TreeNode(6)
        expected_root.left.left = TreeNode(1)
        expected_root.left.right = TreeNode(3)
        expected_root.right.left = TreeNode(5)
        expected_root.right.right = TreeNode(7)
        self.assertTrue(compare_trees(root, expected_root))


    def test_non_complete_tree(self):
        # Setup
        serialized_data = [[4], [2, None], [None, 3]]

        # Exercise
        root = construct_tree(serialized_data)

        # Verify
        expected_root = TreeNode(4)
        expected_root.left = TreeNode(2)
        expected_root.left.right = TreeNode(3)
        self.assertTrue(compare_trees(root, expected_root))

    def test_non_complete_tree_complicated(self):
        # Setup
        serialized_data = [[5], [4, 7], [3, None, 2, None], [-1, None, 9]]

        # Exercise
        root = construct_tree(serialized_data)

        # Verify
        expected_root = TreeNode(5)
        expected_root.left = TreeNode(4)
        expected_root.right = TreeNode(7)
        expected_root.left.left = TreeNode(3)
        expected_root.right.left = TreeNode(2)
        expected_root.left.left.left = TreeNode(-1)
        expected_root.right.left.left = TreeNode(9)
        self.assertTrue(compare_trees(root, expected_root))
