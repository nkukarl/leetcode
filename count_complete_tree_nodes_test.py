from unittest import TestCase

from count_complete_tree_nodes import Solution
from utils_tree import TreeNode


class TestCountCompleteTreeNodes(TestCase):
    def test_count_nodes_4_nodes(self):
        # Setup
        sol = Solution()
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)

        # Exercise
        count = sol.count_nodes(root)

        # Verify
        expected_count = 4
        self.assertEqual(count, expected_count)

    def test_count_nodes_6_nodes(self):
        # Setup
        sol = Solution()
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)

        # Exercise
        count = sol.count_nodes(root)

        # Verify
        expected_count = 6
        self.assertEqual(count, expected_count)

    def test_count_nodes_7_nodes(self):
        # Setup
        sol = Solution()
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        # Exercise
        count = sol.count_nodes(root)

        # Verify
        expected_count = 7
        self.assertEqual(count, expected_count)
