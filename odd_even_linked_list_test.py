import random
from unittest import TestCase

from odd_even_linked_list import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestOddEvenList(TestCase):
    def test_odd_even_list(self):
        # Setup
        sol = Solution()
        linked_list_raw = [x for x in range(1, random.randint(1, 9))]
        random.shuffle(linked_list_raw)
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.odd_even_list(head)

        # Verify
        expected_head = \
            get_head_linked_list(linked_list_raw[::2] + linked_list_raw[1::2])
        self.assertTrue(compare_linked_lists(head, expected_head))
