from unittest import TestCase

from binary_tree_zigzag_level_order_traversal import Solution
from utils_tree import construct_tree


class TestBinaryTreeZigzagLevelOrderTraversal(TestCase):
    def test_zigzag_level_order(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.zigzag_level_order(root)

        # Verify
        expected_ans = [[4], [6, 2], [1, 3, 5, 7]]
        self.assertEqual(ans, expected_ans)
