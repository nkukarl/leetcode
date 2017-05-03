from unittest import TestCase

from remove_nth_node_from_end_of_list import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestRemoveNthNodeFromEndOfList(TestCase):
    def test_remove_nth_from_end(self):
        # Setup
        sol = Solution()
        N = 5
        linked_list_raw = [n for n in range(1, N + 1)]

        # Exercise and Verify
        for n in range(1, N + 1):
            head = get_head_linked_list(linked_list_raw)
            head = sol.remove_nth_from_end(head, n)
            expected_linked_list_raw = linked_list_raw[:-n]
            if n != 1:
                expected_linked_list_raw += linked_list_raw[-(n - 1):]
            expected_head = get_head_linked_list(expected_linked_list_raw)
            self.assertTrue(compare_linked_lists(head, expected_head))
