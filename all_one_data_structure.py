class DoublyLinkedList(object):
    def __init__(self, key):
        self.keys = {key}
        self.prev = None
        self.next = None


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = DoublyLinkedList('head')
        self.tail = DoublyLinkedList('tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_map = {}
        self.count_map = {}

    def inc(self, key):
        """
        Inserts a new key with value 1.
        Or increases the value of an existing key by 1.
        """
        if 0 == self.key_map.get(key, 0):
            self.key_map[key] = 1
            if 1 in self.count_map:
                node = self.count_map[1]
                node.keys.add(key)
            else:
                node = DoublyLinkedList(key)
                self.count_map[1] = node
                next_ = self.head.next
                self.head.next = node
                node.prev = self.head
                node.next = next_
                next_.prev = node
        else:
            count = self.key_map[key]
            self.key_map[key] += 1
            node = self.count_map[count]
            if count + 1 in self.count_map:
                self.count_map[count + 1].keys.add(key)
            else:
                node_ = DoublyLinkedList(key)
                self.count_map[count + 1] = node_
                next_ = node.next
                node.next = node_
                node_.prev = node
                node_.next = next_
                next_.prev = node_

            node.keys.remove(key)
            if 0 == len(node.keys):
                prev_ = node.prev
                next_ = node.next
                prev_.next = next_
                next_.prev = prev_
                del self.count_map[count]

    def dec(self, key):
        """
        Decrease the value of an existing key by 1.
        If the value is 1, remove it from the data structure.
        """
        if key not in self.key_map:
            return
        count = self.key_map[key]
        if 1 == count:
            del self.key_map[key]
        else:
            self.key_map[key] -= 1
        node = self.count_map[count]
        if count - 1 != 0:
            if count - 1 in self.count_map:
                self.count_map[count - 1].keys.add(key)
            else:
                node_ = DoublyLinkedList(key)
                self.count_map[count - 1] = node_
                prev_ = node.prev
                node.prev = node_
                node_.next = node
                node_.prev = prev_
                prev_.next = node_

        node.keys.remove(key)
        if 0 == len(node.keys):
            prev_ = node.prev
            next_ = node.next
            prev_.next = next_
            next_.prev = prev_
            del self.count_map[count]

    def get_max_key(self):
        """
        Returns one of the keys with maximal value.
        """
        keys = self.tail.prev.keys
        for key in keys:
            return key
        return ''

    def get_min_key(self):
        """
        Returns one of the keys with minimal value.
        """
        keys = self.head.next.keys
        for key in keys:
            return key
        return ''
