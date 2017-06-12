from unittest import TestCase

from convert_sorted_list_to_binary_search_tree import Solution
from utils_linked_list import get_head_linked_list
from utils_tree import compare_trees, construct_tree


class TestConvertSortedListToBinarySearchTree(TestCase):
    def test_sorted_list_to_bst(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4, 5, 6, 7]
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        root = sol.sorted_list_to_bst(head)
        expected_root = construct_tree(serialized_data)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
