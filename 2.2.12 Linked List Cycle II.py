class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def detectCycle(self, head):
		slow, fast = head, head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				node = head
				while slow != node:
					slow = slow.next
					node = node.next
				return node
		return None

nodes = [ListNode(val) for val in range(10)]
for i in range(len(nodes) - 1):
	nodes[i].next = nodes[i + 1]
nodes[-1].next = nodes[4]
head = nodes[0]

inst = Solution()
print(inst.detectCycle(head).val)