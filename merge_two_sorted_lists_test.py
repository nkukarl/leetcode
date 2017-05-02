from unittest import TestCase

from nose_parameterized import parameterized

from merge_two_sorted_lists import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestMergeTwoSortedLists(TestCase):
    @parameterized.expand([
        [
            [],
            [],
        ],
        [
            [],
            [1, 2, 3, 4],
        ],
        [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
        ],
        [
            [1, 2, 3, 4],
            [-4, -3, -2, -1],
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 8],
        ],
    ])
    def test_merge_two_lists(self, l1_raw, l2_raw):
        # Setup
        sol = Solution()
        l1 = get_head_linked_list(l1_raw)
        l2 = get_head_linked_list(l2_raw)

        # Exercise
        head = sol.merge_two_lists(l1, l2)

        # Verify
        expected_head = get_head_linked_list(sorted(l1_raw + l2_raw))
        self.assertTrue(compare_linked_lists(head, expected_head))
