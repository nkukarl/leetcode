import random
from unittest import TestCase

from print_a_linked_list_in_reverse_order import Solution
from utils_linked_list import get_head_linked_list


class TestPrintALinkedListInReverseOrder(TestCase):
    def test_print_in_reverse(self):
        # Setup
        sol = Solution()
        linked_list_raw = [random.randint(1, 9) for _ in range(9)]
        head = get_head_linked_list(linked_list_raw)

        # Exercise and Verify
        print('\nObtained:', end=' ')
        sol.print_in_reverse(head)
        print('\nExpected:', end=' ')
        for n in linked_list_raw[::-1]:
            print(n, end=' ')
