from unittest import TestCase

from nose_parameterized import parameterized

from insertion_sort_list import Solution
from utils_linked_list import get_head_linked_list, compare_linked_lists


class TestInsertionSortList(TestCase):
    @parameterized.expand([
        [
            [],
        ],
        [
            [1],
        ],
        [
            [3, 5, 4, 2, 1],
        ],
        [
            [1, 3, 2, 5, 4],
        ],
    ])
    def test_insertion_sort_list(self, linked_list_raw):
        # Setup
        sol = Solution()
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.insertion_sort_list(head)

        # Verify
        expected_head = get_head_linked_list(sorted(linked_list_raw))
        self.assertTrue(compare_linked_lists(head, expected_head))
