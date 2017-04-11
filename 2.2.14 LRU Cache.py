class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity):
        self.summary = dict()
        self.capacity = capacity
        self.size = 0
        self.dummy = DoublyLinkedListNode(-1, -1)
        self.tail = self.dummy

    def get(self, key):
        if key not in self.summary:
            return -1
        entry = self.summary[key]
        self.update(entry)
        return entry.val

    def update(self, entry):
        if entry != self.tail:
            prev, next = entry.prev, entry.next
            prev.next = next
            next.prev = prev
            entry.next = None
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry

    def set(self, key, val):
        if key in self.summary:
            entry = self.summary[key]
            entry.val = val
            self.update(entry)
            return
        entry = DoublyLinkedListNode(key, val)
        self.summary[key] = entry
        self.tail.next = entry
        entry.prev = self.tail
        self.tail = entry
        if self.size < self.capacity:
            self.size += 1
            return
        head = self.dummy.next
        if head:
            self.dummy.next = head.next
            head.next.prev = self.dummy
            del self.summary[head.key]


cache = LRUCache(5)
cache.set(1, 4)
print(cache.get(1))
cache.set(3, 5)
print(cache.get(3))
cache.set(3, 6)
print(cache.get(3))
print(cache.get(1))
cache.set(4, 1)
cache.set(5, 3)
cache.set(6, 2)
cache.set(7, 9)

print(cache.get(4))
