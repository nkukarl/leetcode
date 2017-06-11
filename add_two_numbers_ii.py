from utils_linked_list import ListNode


class Solution(object):
    def add_two_numbers(self, head1, head2):
        l1, l2 = self.get_length(head1), self.get_length(head2)
        if l1 == l2:
            head_raw, carry = self.add_two_lists(head1, head2)
            if 1 == carry:
                head = ListNode(1)
                head.next = head_raw
            else:
                head = head_raw
            return head

        if l1 < l2:
            head1, head2 = head2, head1

        prev_ = None
        node_ = head1
        diff = abs(l1 - l2)
        while diff > 0:
            prev_ = node_
            node_ = node_.next
            diff -= 1

        # Split the first list into two lists
        node, carry = self.add_two_lists(node_, head2)
        if 1 == carry:
            head_raw, carry_, last = self.add_one_to_a_list(head1, prev_)
            if 1 == carry_:
                head = ListNode(1)
                head.next = head_raw
            else:
                head = head_raw
        else:
            head, last = self.copy_a_list(head1, prev_)
        # Relink the two lists separated from the first list
        last.next = node
        return head

    def add_two_lists(self, head1, head2):
        if head1 is None and head2 is None:
            return None, 0
        next_, carry = self.add_two_lists(head1.next, head2.next)
        sum_ = carry + head1.val + head2.val
        node = ListNode(sum_ % 10)
        node.next = next_
        return node, sum_ // 10

    def add_one_to_a_list(self, head, tail):
        if head == tail.next:
            return None, 1, None
        next_, carry, last = self.add_one_to_a_list(head.next, tail)
        sum_ = carry + head.val
        node = ListNode(sum_ % 10)
        node.next = next_
        if last is None:
            return node, sum_ // 10, node
        return node, sum_ // 10, last

    def copy_a_list(self, head, tail):
        if head == tail.next:
            return None, None
        next_, last = self.copy_a_list(head.next, tail)
        node = ListNode(head.val)
        node.next = next_
        if last is None:
            return node, node
        return node, last

    def get_length(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
