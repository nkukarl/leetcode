from unittest import TestCase

from binary_tree_right_side_view import Solution
from utils_tree import construct_tree


class TestBinaryTreeRightSideView(TestCase):
    def test_right_side_view(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.right_side_view(root)
        expected_ans = [4, 6, 7]

        # Verify
        self.assertEqual(ans, expected_ans)
