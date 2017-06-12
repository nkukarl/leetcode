from unittest import TestCase

from binary_tree_level_order_traversal import Solution
from utils_tree import construct_tree


class TestBinaryTreeLevelOrderTraversal(TestCase):
    def test_level_order(self):
        # Setup
        sol = Solution()
        serialize_data = [[1], [2, 3], [4, 5, 6, 7]]
        root = construct_tree(serialize_data)

        # Exercise
        ans = sol.level_order(root)

        # Verify
        self.assertEqual(ans, serialize_data)
