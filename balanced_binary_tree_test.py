from unittest import TestCase

from balanced_binary_tree import Solution
from utils_tree import construct_tree


class TestBalancedBinaryTree(TestCase):
    def test_is_balanced(self):
        # Setup
        sol = Solution()
        serialized_data = [[3], [2, 4], [1]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.is_balanced(root)

        # Verify
        self.assertTrue(ans)
