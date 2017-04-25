from unittest import TestCase

from balanced_binary_tree import Solution
from utils_tree import get_root_tree


class TestBalancedBinaryTree(TestCase):
    def test_is_balanced(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.is_balanced(root)

        # Verify
        self.assertTrue(ans)
