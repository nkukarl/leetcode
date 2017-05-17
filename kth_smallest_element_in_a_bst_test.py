from unittest import TestCase

from kth_smallest_element_in_a_bst import Solution
from utils_tree import get_root_tree


class TestKthSmallestElementInABST(TestCase):
    def test_kth_smallest(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)

        # Exercise and Verify
        for k in tree_raw:
            ans = sol.kth_smallest(root, k)
            self.assertEqual(ans, k)
