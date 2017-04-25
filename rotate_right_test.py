from unittest import TestCase

from rotate_right import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestRotateRight(TestCase):
    def test_rotate_right(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4, 5, 6, 7]
        head = get_head_linked_list(linked_list_raw)
        k = 3

        # Exercise
        head = sol.rotate_right(head, k)
        expected_head = get_head_linked_list([5, 6, 7, 1, 2, 3, 4])

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
