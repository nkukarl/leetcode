from unittest import TestCase

from sum_root_to_leaf_numbers import Solution
from utils_tree import construct_tree


class TestSumRootToLeafNumbers(TestCase):
    def test_sum_numbers(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.sum_numbers(root)
        expected_ans = 421 + 423 + 465 + 467

        # Verify
        self.assertEqual(ans, expected_ans)
