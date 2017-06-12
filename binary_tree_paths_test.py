from unittest import TestCase

from binary_tree_paths import Solution
from utils_tree import construct_tree


class TestBinaryTreePaths(TestCase):
    def test_binary_tree_paths(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.binary_tree_paths(root)
        expected_ans = [
            '4->2->1',
            '4->2->3',
            '4->6->5',
            '4->6->7',
        ]

        # Verify
        self.assertEqual(ans, expected_ans)
