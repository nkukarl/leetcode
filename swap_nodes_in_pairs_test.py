from unittest import TestCase

from nose_parameterized import parameterized

from swap_nodes_in_pairs import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestSwapNodeInPairs(TestCase):
    @parameterized.expand([
        [
            [],
            [],
        ],
        [
            [1],
            [1],
        ],
        [
            [1, 2],
            [2, 1],
        ],
        [
            [1, 2, 3],
            [2, 1, 3],
        ],
        [
            [1, 2, 3, 4],
            [2, 1, 4, 3],
        ],
    ])
    def test_swap_pairs(self, linked_list_raw, expected_linked_list_raw):
        # Setup
        sol = Solution()
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.swap_pairs(head)

        # Verify
        expected_head = get_head_linked_list(expected_linked_list_raw)
        self.assertTrue(compare_linked_lists(head, expected_head))
