from unittest import TestCase

from diameter_of_binary_tree import Solution
from utils_tree import get_root_tree


class TestDiameterOfBinaryTree(TestCase):
    def test_diameter_of_binary_tree(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.diameter_of_binary_tree(root)

        # Verify
        expected_ans = 4
        self.assertEqual(ans, expected_ans)
