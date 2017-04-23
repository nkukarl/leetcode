import random
from unittest import TestCase

from remove_linked_list_elements import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestRemoveLinkedListElements(TestCase):
    def test_remove_elements(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4] * 5
        random.shuffle(linked_list_raw)
        val = random.randint(1, 4)
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.remove_elements(head, val)
        while val in linked_list_raw:
            linked_list_raw.remove(val)
        expected_head = get_head_linked_list(linked_list_raw)

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
