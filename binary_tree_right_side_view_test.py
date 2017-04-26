from unittest import TestCase

from binary_tree_right_side_view import Solution
from utils_tree import get_root_tree


class TestBinaryTreeRightSideView(TestCase):
    def test_right_side_view(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.right_side_view(root)
        expected_ans = [4, 6, 7]

        # Verify
        self.assertEqual(ans, expected_ans)
