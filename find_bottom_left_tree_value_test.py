from unittest import TestCase

from find_bottom_left_tree_value import Solution
from utils_tree import get_root_tree


class TestFindBottomLeftTreeValue(TestCase):
    def test_find_bottom_left_value(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.find_bottom_left_value(root)

        # Verify
        expected_ans = root.left.left.val
        self.assertEqual(ans, expected_ans)
