class TreeLinkNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
		self.next = None

class Solution:
	def sumNumbers(self, root):
		self.paths = []
		self.ans = 0
		self.helper(root, [], 0)
		print(self.paths)
		return self.ans

	def helper(self, root, cur, curVal):
		if root:
			if not root.left and not root.right:
				self.ans += curVal * 10 + root.val
				self.paths.append(cur + [root.val])
			else:
				self.helper(root.left, cur + [root.val], curVal * 10 + root.val)
				self.helper(root.right, cur + [root.val], curVal * 10 + root.val)


root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

inst = Solution()
print(inst.sumNumbers(root))