class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def rotateRight(self, head, k):
		n, tail = self.getLength(head)
		k %= n
		if k == 0:
			return head
		counter = 0
		prev = None
		cur = head
		while counter < n - k:
			prev = cur
			cur = cur.next
			counter += 1
		tail.next = head
		prev.next = None
		return cur

	def getLength(self, head):
		length = 0
		prev = None
		while head:
			length += 1
			prev = head
			head = head.next
		return length, prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

inst = Solution()
head = inst.rotateRight(head, 1)

while head:
	print(head.val, end = ' ')
	head = head.next
print()