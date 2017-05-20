class DoublyLinkedListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.DICT = {}
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.DICT:
            return -1

        # Key in self.DICT, node exist
        node = self.DICT[key]

        # Get node and link node.prev and node.next
        prev_ = node.prev
        next_ = node.next
        prev_.next = next_
        next_.prev = prev_

        # Set node as the last node
        last = self.tail.prev
        last.next = node
        node.prev = last
        self.tail.prev = node
        node.next = self.tail

        return node.val

    def put(self, key, value):
        if key in self.DICT:
            # Get node
            node = self.DICT[key]
            # Update value
            node.val = value
            # Pretend to get key so that the list can be reconstructed
            self.get(key)
        else:
            # Create a new node
            node = DoublyLinkedListNode(key, value)
            # Add a new entry in DICT for the new node
            self.DICT[key] = node
            # Set the new node as the last node
            last = self.tail.prev
            last.next = node
            node.prev = last
            self.tail.prev = node
            node.next = self.tail
            # If capacity is reached
            if len(self.DICT) > self.capacity:
                # Get node to be deleted
                node = self.head.next
                # Delete mapping from DICT
                self.DICT.pop(node.key)
                # Set second node as the first
                first = self.head.next
                second = first.next
                self.head.next = second
                second.prev = self.head
