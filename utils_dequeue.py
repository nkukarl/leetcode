class DoublyLinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class Dequeue(object):
    def __init__(self):
        self.head = DoublyLinkedListNode(None)
        self.tail = DoublyLinkedListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def is_empty(self):
        return 0 == self.count

    def append(self, val):
        node = DoublyLinkedListNode(val)
        self.count += 1

        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def append_left(self, val):
        node = DoublyLinkedListNode(val)
        self.count += 1

        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.count -= 1

        last = self.tail.prev

        prev_ = last.prev
        prev_.next = self.tail
        self.tail.prev = prev_

        return last.val

    def pop_left(self):
        if self.is_empty():
            raise IndexError
        self.count -= 1

        first = self.head.next

        next_ = first.next
        self.head.next = next_
        next_.prev = self.head

        return first.val

    def get(self, index):
        if self.is_empty() or index not in [0, -1]:
            raise IndexError
        if 0 == index:
            return self.head.next.val
        return self.tail.prev.val
