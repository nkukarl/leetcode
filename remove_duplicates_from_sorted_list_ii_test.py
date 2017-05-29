from unittest import TestCase

from nose_parameterized import parameterized

from remove_duplicates_from_sorted_list_ii import Solution
from utils_linked_list import get_head_linked_list, compare_linked_lists


class TestRemoveDuplicatesFromSortedListII(TestCase):
    @parameterized.expand([
        [
            [],
        ],
        [
            [1],
        ],
        [
            [1, 1, 1, 2, 3],
        ],
        [
            [1, 2, 3, 3, 4, 4, 5],
        ],
    ])
    def test_delete_duplicates(self, linked_list_raw):
        # Setup
        sol = Solution()
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.delete_duplicates(head)

        # Verify
        expected_head = \
            get_head_linked_list(self.delete_duplicates(linked_list_raw))
        self.assertTrue(compare_linked_lists(head, expected_head))

    def delete_duplicates(self, link_list_raw):
        summary = {}
        for val in link_list_raw:
            summary[val] = summary.get(val, 0) + 1

        ans = []
        for val in link_list_raw:
            if 1 == summary[val]:
                ans.append(val)

        return ans
