from unittest import TestCase

from find_bottom_left_tree_value import Solution
from utils_tree import construct_tree


class TestFindBottomLeftTreeValue(TestCase):
    def test_find_bottom_left_value(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.find_bottom_left_value(root)

        # Verify
        expected_ans = root.left.left.val
        self.assertEqual(ans, expected_ans)
