import random
from unittest import TestCase

from minimum_absolute_difference_in_bst import Solution
from utils_tree import get_root_tree


class TestMinimumAbsoluteDifferenceInBST(TestCase):
    def test_get_minimum_difference(self):
        # Setup
        sol = Solution()
        tree_raw = sorted(random.sample(list(range(1000)), 7))
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.get_minimum_difference(root)

        # Verify
        expected_ans = \
            min([n1 - n2 for n1, n2 in zip(tree_raw[1:], tree_raw[:-1])])
        self.assertEqual(ans, expected_ans)
