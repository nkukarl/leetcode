from utils_linked_list import ListNode


class Solution(object):
    def delete_duplicates(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(head.val - 1)
        tail = dummy
        node = head
        while node is not None:
            if node.next is None:
                tail.next = node
                node = node.next
            else:
                if node.next.val != node.val:
                    next_ = node.next
                    tail.next = node
                    tail = node
                    tail.next = None
                    node = next_
                else:
                    cur_val = node.val
                    while node is not None and node.val == cur_val:
                        node = node.next
        return dummy.next
