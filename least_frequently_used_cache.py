class DoublyLinkedListNode(object):
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = DoublyLinkedListNode(None, None)
        self.tail = DoublyLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_as_last(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def pop_node(self, node):
        prev_ = node.prev
        next_ = node.next
        prev_.next = next_
        next_.prev = prev_

    def pop_first_node(self):
        first = self.head.next
        second = first.next
        self.head.next = second
        second.prev = self.head
        return first

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_node = {}
        self.key_count = {}
        self.count_linked_list = {}

    def get(self, key):
        if key not in self.key_node:
            return -1
        # Get current count
        count = self.key_count[key]
        # Increase count by 1
        self.key_count[key] += 1
        # Get node
        node = self.key_node[key]
        # Get the old linked list corresponding to current count
        linked_list_old = self.count_linked_list[count]
        # Remove node from the old linked list
        linked_list_old.pop_node(node)
        # Delete entry from count_linked_list if the old linked list is empty
        if linked_list_old.is_empty():
            self.count_linked_list.pop(count)
        # Get the new linked list, if it does not exist, create one
        linked_list_new = \
            self.count_linked_list.get(count + 1, DoublyLinkedList())
        linked_list_new.add_node_as_last(node)
        # Update count_linked_list
        self.count_linked_list[count + 1] = linked_list_new
        # Return value of node
        return node.value

    def put(self, key, value):
        if 0 == self.capacity:
            return
        if key in self.key_node:
            # Just an update of value
            node = self.key_node[key]
            node.value = value
            # Pretend to get node by key to update the count and etc
            self.get(key)
        else:
            # If capacity is reached
            if len(self.key_node) == self.capacity:
                # TODO: How to get count_min in O(1)?
                # Get count_min
                count_min = min(self.count_linked_list.keys())
                # Get linked_list corresponding to count = count_min
                linked_list = self.count_linked_list[count_min]
                # Pop first node from linked_list
                lru_node = linked_list.pop_first_node()
                # Delete linked_list entry from count_linked_list if empty
                if linked_list.is_empty():
                    self.count_linked_list.pop(count_min)
                # Update key_node and key_count map
                self.key_node.pop(lru_node.key)
                self.key_count.pop(lru_node.key)

            # Create a new node
            node = DoublyLinkedListNode(key, value)
            # Update key_node and key_count map
            self.key_node[key] = node
            self.key_count[key] = 1

            # Get linked+list corresponding to count = 1
            linked_list = self.count_linked_list.get(1, DoublyLinkedList())
            # Add node to linked list
            linked_list.add_node_as_last(node)
            # Update count_linked_list
            self.count_linked_list[1] = linked_list
