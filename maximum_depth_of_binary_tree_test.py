from unittest import TestCase

from maximum_depth_of_binary_tree import Solution
from utils_tree import construct_tree


class TestMaximumDepthOfBinaryTree(TestCase):
    def test_max_depth(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.max_depth(root)

        # Verify
        expected_ans = 3
        self.assertEqual(ans, expected_ans)
