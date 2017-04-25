from unittest import TestCase

from sum_root_to_leaf_numbers import Solution
from utils_tree import get_root_tree


class TestSumRootToLeafNumbers(TestCase):
    def test_sum_numbers(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.sum_numbers(root)
        expected_ans = 421 + 423 + 465 + 467

        # Verify
        self.assertEqual(ans, expected_ans)
