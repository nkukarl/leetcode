from unittest import TestCase

from binary_tree_zigzag_level_order_traversal import Solution
from utils_tree import get_root_tree


class TestBinaryTreeZigzagLevelOrderTraversal(TestCase):
    def test_zigzag_level_order(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.zigzag_level_order(root)

        # Verify
        expected_ans = [[4], [6, 2], [1, 3, 5, 7]]
        self.assertEqual(ans, expected_ans)
