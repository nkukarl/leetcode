from unittest import TestCase

from linked_list_cycle import Solution
from utils_linked_list import get_head_linked_list, retrieve_tail_linked_list


class TestLinkedListCycle(TestCase):
    def test_without_cycle(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4, 5, 6, 7]
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        flag = sol.has_cycle(head)
        node = sol.detect_cycle(head)

        # Verify
        self.assertFalse(flag)
        self.assertIsNone(node)

    def test_with_cycle(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4, 5, 6, 7]
        head = get_head_linked_list(linked_list_raw)
        tail = retrieve_tail_linked_list(head)
        tail.next = head.next.next

        # Exercise
        flag = sol.has_cycle(head)
        node = sol.detect_cycle(head)

        # Verify
        self.assertTrue(flag)
        self.assertEqual(node, head.next.next)
