class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1, l2):
		n1, n2 = l1, l2
		carry = 0
		dummy = ListNode(0)
		n = dummy
		while n1 and n2:
			val = (n1.val + n2.val + carry) % 10
			carry = (n1.val + n2.val + carry) // 10
			n.next = ListNode(val)
			n1 = n1.next
			n2 = n2.next
			n = n.next
		while n1:
			val = (n1.val + carry) % 10
			carry = n1
			n.next = ListNode(val)
			n1 = n1.next
			n = n.next
		while n2:
			val = (n2.val + carry) % 10
			carry = n2
			n.next = ListNode(val)
			n2 = n2.next
			n = n.next
		if carry:
			n.next = ListNode(1)
		
		return dummy.next

l1 = ListNode(9, ListNode(9, ListNode(9)))
l2 = ListNode(9, ListNode(9, ListNode(9)))

inst = Solution()
l = inst.addTwoNumbers(l1, l2)

while l:
	print(l.val, end = ' ')
	l = l.next
print()