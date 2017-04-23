import random
from unittest import TestCase

from add_two_numbers_ii import Solution
from utils_linked_list import \
    compare_linked_lists, get_head_linked_list, ListNode


class TestAddTwoNumbers(TestCase):
    def setup(self):

        num1, num2 = random.randint(1, 999), random.randint(1, 999)
        head1 = get_head_linked_list(list(map(int, str(num1))))
        head2 = get_head_linked_list(list(map(int, str(num2))))
        return head1, head2, num1, num2

    def test_add_two_numbers_1(self):
        # Setup
        sol = Solution()
        head1, head2, _, _ = self.setup()

        # Exercise
        head = sol.add_two_numbers(head1, head2)
        expected_head = self.add_two_numbers_1(head1, head2)

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))

    def add_two_numbers_1(self, head1, head2):
        n1, n2 = self._get_number(head1), self._get_number(head2)
        return self._get_list(n1 + n2)

    def _get_number(self, head):
        node = head
        num_str = ''
        while node is not None:
            num_str += str(node.val)
            node = node.next
        return int(num_str)

    def _get_list(self, num):
        num = map(int, str(num))
        dummy = ListNode(0)
        node = dummy
        for n in num:
            node.next = ListNode(n)
            node = node.next
        return dummy.next

    def test_add_two_numbers_2(self):
        # Setup
        sol = Solution()
        head1, head2, _, _ = self.setup()

        # Exercise
        head = sol.add_two_numbers(head1, head2)
        expected_head = self.add_two_numbers_2(head1, head2)

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))

    def add_two_numbers_2(self, head1, head2):
        tail1 = self._reverse_list(head1)
        tail2 = self._reverse_list(head2)
        tail = self._add_reversed_numbers(tail1, tail2)
        return self._reverse_list(tail)

    def _reverse_list(self, head):
        node = head
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
        return prev

    def _add_reversed_numbers(self, tail1, tail2):
        dummy = ListNode(0)
        node = dummy
        node1, node2 = tail1, tail2
        carry = 0
        while node1 is not None or node2 is not None:
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            res = val1 + val2 + carry
            val = res % 10
            carry = res // 10
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None
            node.next = ListNode(val)
            node = node.next
        if 1 == carry:
            node.next = ListNode(1)
        return dummy.next

    def test_add_two_numbers_3(self):
        # Setup
        sol = Solution()
        head1, head2, num1, num2 = self.setup()

        # Exercise
        head = sol.add_two_numbers(head1, head2)
        expected_head = \
            get_head_linked_list(list(map(int, str(num1 + num2))))

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
