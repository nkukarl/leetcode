from unittest import TestCase

from minimum_depth_of_binary_tree import Solution
from utils_tree import construct_tree


class TestMinimumDepthOfBinaryTree(TestCase):
    def test_min_depth(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.min_depth(root)

        # Verify
        expected_ans = 3
        self.assertEqual(ans, expected_ans)
