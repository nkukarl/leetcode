from unittest import TestCase

from binary_tree_tilt import Solution
from utils_tree import get_root_tree


class TestBinaryTreeTilt(TestCase):
    def test_find_tilt(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.find_tilt(root)

        # Verify
        expected_ans = 2
        self.assertEqual(ans, expected_ans)
