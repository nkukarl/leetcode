from unittest import TestCase

from nose_parameterized import parameterized

from merge_k_sorted_lists import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestMergeKSortedLists(TestCase):
    @parameterized.expand([
        [
            [
                [],
                [],
            ],
        ],
        [
            [
                [2, 6, 7],
                [8, 10],
                [1, 3, 5],
                [4, 9],
            ],
        ],
        [
            [
                [1, 1, 2],
                [1, 2, 2],
            ],
        ],
        [
            [
                [-10, -9, -9, -3, -1, -1, 0],
                [-5],
                [4],
                [-8],
                [],
                [-9, -6, -5, -4, -2, 2, 3],
                [-3, -3, -2, -1, 0],
            ]
        ]
    ])
    def test_merge_k_lists(self, linked_lists_raw):
        # Setup
        sol = Solution()

        # Exercise
        linked_lists, linked_list_raw = [], []
        for llr in linked_lists_raw:
            linked_lists.append(get_head_linked_list(llr))
            linked_list_raw.extend(llr)
        head = sol.merge_k_lists(linked_lists)

        # Verify
        expected_head = get_head_linked_list(sorted(linked_list_raw))
        self.assertTrue(compare_linked_lists(head, expected_head))
