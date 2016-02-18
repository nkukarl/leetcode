class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def buildTree(self, inorder, postorder):
		if not inorder or not postorder:
			return None
		val = postorder[-1]
		root = TreeNode(val)
		pos = inorder.index(val)
		inLeft = inorder[:pos]
		inRight = inorder[pos + 1:]
		postLeft = postorder[:pos]
		postRight = postorder[pos : -1]
		root.left = self.buildTree(inLeft, postLeft)
		root.right = self.buildTree(inRight, postRight)
		return root

inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

inst = Solution()
root = inst.buildTree(inorder, postorder)