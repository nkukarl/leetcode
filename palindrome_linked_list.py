from utils_linked_list import ListNode


class Solution(object):
    def is_palindrome(self, head):
        """

        Args:
            head (ListNode): head of linked list

        Returns:
            bool

        """
        length = self.get_length(head)
        if length in [0, 1]:
            return True
        if 2 == length:
            return head.val == head.next.val

        mid = self.split(head, length)
        tail = self.reverse(mid)
        return self.compare_linked_lists(head, tail)

    def get_length(self, head):
        """

        Args:
            head (ListNode): head of linked list

        Returns:
            length of linked list

        """
        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def split(self, head, length):
        """

        Args:
            head (ListNode): head of linked list
            length (int): length of linked list

        Returns:
            head, mid point

        """
        n = length // 2
        node = head
        prev = None
        while n:
            prev = node
            node = node.next
            n -= 1
        mid = node
        if 1 == length % 2:
            # If length is an odd number, skip the true mid point
            # and move to the next
            mid = mid.next
        prev.next = None
        return mid

    def reverse(self, head):
        """

        Args:
            head (ListNode): head of linked list

        Returns:
            tail

        """
        node = head
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
        return prev

    def compare_linked_lists(self, head1, head2):
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
