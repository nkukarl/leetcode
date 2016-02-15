class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def deleteDuplicates(self, head):
		dummy = ListNode(head.val - 1, head)
		cur = dummy
		slow = dummy.next
		fast = slow.next
		while fast:
			if fast.val == slow.val:
				while fast and fast.val == slow.val:
					fast = fast.next
				if fast:
					slow = fast
					fast = slow.next
				else:
					cur.next = None
					return dummy.next
			else:
				cur.next = slow
				cur = cur.next
				slow = cur.next
				fast = slow.next
		return dummy.next

head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(4, ListNode(6, ListNode(6, ListNode(6, ListNode(7, ListNode(8))))))))))))

inst = Solution()
head = inst.deleteDuplicates(head)

while head:
	print(head.val, end = ' ')
	head = head.next
print()
