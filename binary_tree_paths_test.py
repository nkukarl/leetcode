from unittest import TestCase

from binary_tree_paths import Solution
from utils_tree import get_root_tree


class TestBinaryTreePaths(TestCase):
    def test_binary_tree_paths(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

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
