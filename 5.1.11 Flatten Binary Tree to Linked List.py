class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def flatten(self, root):
		if not root:
			return None
		if not root.left:
			root.right = self.flatten(root.right)
		elif not root.right:
			root.right = self.flatten(root.left)
			root.left = None
		else:
			L, R = self.flatten(root.left), self.flatten(root.right)
			root.left = None
			root.right = L
			prev = None
			node = L
			while node:
				prev = node
				node = node.right
			prev.right = R
		return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

inst = Solution()
root = inst.flatten(root)