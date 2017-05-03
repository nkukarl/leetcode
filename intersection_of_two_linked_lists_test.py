import random
from unittest import TestCase

from intersection_of_two_linked_lists import Solution
from utils_linked_list import get_head_linked_list


class TestIntersectionOfTwoLinkedLists(TestCase):
    def test_get_intersection_node(self):
        # Setup
        sol = Solution()
        N = 5
        N1, N2 = random.randint(1, N), random.randint(1, N)
        node_common = get_head_linked_list(
            [random.randint(1, N) for _ in range(N)])
        head_1 = get_head_linked_list(
            [random.randint(1, N) for _ in range(N1)])
        tail_1 = self.get_tail(head_1)
        head_2 = get_head_linked_list(
            [random.randint(1, N) for _ in range(N2)])
        tail_2 = self.get_tail(head_2)
        tail_1.next = node_common
        tail_2.next = node_common

        # Exercise
        node = sol.get_intersection_node(head_1, head_2)
        expected_node = node_common

        # Verify
        self.assertEqual(node, expected_node)

    def get_tail(self, head):
        node = head
        while node.next is not None:
            node = node.next
        return node

