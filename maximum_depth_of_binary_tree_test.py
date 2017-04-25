from unittest import TestCase

from maximum_depth_of_binary_tree import Solution
from utils_tree import get_root_tree


class TestMaximumDepthOfBinaryTree(TestCase):
    def test_max_depth(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.max_depth(root)

        # Verify
        expected_ans = 3
        self.assertEqual(ans, expected_ans)
