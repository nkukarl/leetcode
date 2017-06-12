from unittest import TestCase

from kth_smallest_element_in_a_bst import Solution
from utils_tree import construct_tree


class TestKthSmallestElementInABST(TestCase):
    def test_kth_smallest(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise and Verify
        for k in [1, 2, 3, 4, 5, 6, 7]:
            ans = sol.kth_smallest(root, k)
            self.assertEqual(ans, k)
