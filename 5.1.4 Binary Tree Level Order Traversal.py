class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def levelOrderTraversal(self, root):
		self.res = []
		self.helper(root, 0)

		return self.res

	def helper(self, root, level):
		if root:
			if level < len(self.res):
				self.res[level].append(root.val)
			else:
				self.res.append([root.val])
			self.helper(root.left, level + 1)
			self.helper(root.right, level + 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

inst = Solution()
print(inst.levelOrderTraversal(root))