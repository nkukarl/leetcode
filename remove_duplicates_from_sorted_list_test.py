from unittest import TestCase

from nose_parameterized import parameterized

from remove_duplicates_from_sorted_list import Solution
from utils_linked_list import get_head_linked_list, compare_linked_lists


class TestRemoveDuplicatesFromSortedList(TestCase):
    @parameterized.expand([
        [
            [],
        ],
        [
            [1],
        ],
        [
            [1, 2, 2, 2, 3, 3, 4, 5, 6, 6],
        ],
        [
            [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7],
        ],
    ])
    def test_delete_duplicates(self, linked_list_raw):
        # Setup
        sol = Solution()
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.delete_duplicates(head)

        # Verify
        expected_head = get_head_linked_list(sorted(list(set(linked_list_raw))))
        self.assertTrue(compare_linked_lists(head, expected_head))
