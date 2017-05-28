class Solution(object):
    def insertion_sort_list(self, head):
        if head is None or head.next is None:
            return head
        node = head.next
        head.next = None
        tail = head
        while node is not None:
            next_ = node.next
            if node.val <= head.val:
                node.next = head
                head = node
            elif node.val >= tail.val:
                tail.next = node
                tail = node
                node.next = None
            else:
                node.next = None
                self.insert(head, node)
            node = next_
        return head

    def insert(self, head, node_ins):
        node = head
        while node.next is not None:
            if node.val <= node_ins.val <= node.next.val:
                next_ = node.next
                node.next = node_ins
                node_ins.next = next_
                break
            else:
                node = node.next
