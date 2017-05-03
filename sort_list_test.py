import random
from unittest import TestCase

from sort_list import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestSortList(TestCase):
    def test_sort_list(self):
        # Setup
        sol = Solution()
        linked_list_raw = [i for i in range(1000)]
        random.shuffle(linked_list_raw)
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.sort_list(head)
        expected_head = get_head_linked_list(sorted(linked_list_raw))

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
