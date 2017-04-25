class Solution(object):
    def rotate_right(self, head, k):
        length, tail = self.get_length_and_tail(head)
        if length <= 1:
            return head
        k %= length
        if 0 == k:
            return head
        m = length - k
        new_head = self.split(head, m)
        tail.next = head
        return new_head

    def get_length_and_tail(self, head):
        tail = None
        length = 0
        node = head
        while node is not None:
            length += 1
            tail = node
            node = node.next
        return length, tail

    def split(self, head, m):
        prev = None
        node = head
        while m > 0:
            prev = node
            node = node.next
            m -= 1
        prev.next = None
        return node
