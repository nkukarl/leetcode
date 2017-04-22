import random
from unittest import TestCase

from remove_linked_list_elements import ListNode, Solution


class TestRemoveLinkedListElements(TestCase):
    def test_remove_elements(self):
        # Setup
        sol = Solution()
        linked_list_raw = [1, 2, 3, 4] * 5
        random.shuffle(linked_list_raw)
        val = random.randint(1, 4)
        head = self.get_head(linked_list_raw)

        # Exercise
        head = sol.remove_elements(head, val)
        while val in linked_list_raw:
            linked_list_raw.remove(val)
        expected_head = self.get_head(linked_list_raw)

        # Verify
        self.assertTrue(self.compare(head, expected_head))

    def get_head(self, linked_list_raw):
        if 0 == len(linked_list_raw):
            return None
        head = ListNode(linked_list_raw[0])
        node = head
        for val in linked_list_raw[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

    def compare(self, head1, head2):
        """

        Args:
            head1 (ListNode): head of linked list
            head2 (ListNode): head of linked list

        Returns:
            bool

        """
        if head1 is None and head2 is None:
            return True
        node1, node2 = head1, head2
        while node1 is not None and node2 is not None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        if node1 is not None or node2 is not None:
            return False
        return True
