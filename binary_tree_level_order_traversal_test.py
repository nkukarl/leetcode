from unittest import TestCase

from binary_tree_level_order_traversal import Solution
from utils_tree import get_root_tree


class TestBinaryTreeLevelOrderTraversal(TestCase):
    def test_level_order(self):
        # Setup
        sol = Solution()
        tree_raw = [4, 2, 5, 1, 6, 3, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.level_order(root)

        # Verify
        expected_ans = [[1], [2, 3], [4, 5, 6, 7]]
        self.assertEqual(ans, expected_ans)
