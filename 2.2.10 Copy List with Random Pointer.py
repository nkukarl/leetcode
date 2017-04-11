class RandomListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next, self.random = next, None


class Solution:
    def copyRandomList(self, head):
        node = head
        while node:
            next = node.next
            node.next = RandomListNode(node.val)
            node.next.next = next
            node = next
        node = head
        while node and node.next:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node = head
        copy = head.next
        while node:
            tmp = node.next
            node.next = tmp.next
            node = node.next
            if node:
                tmp.next = node.next
        return copy


head = RandomListNode(0,
                      RandomListNode(1, RandomListNode(2, RandomListNode(3))))
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next

inst = Solution()
copy = inst.copyRandomList(head)

print(copy.random.val)
print(copy.next.random.val)
print(copy.next.next.random.val)
print(copy.next.next.next.random == None)

while copy:
    print(copy.val, end=' ')
    copy = copy.next
print()
