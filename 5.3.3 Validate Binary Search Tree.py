class Solution:
	def isValidBST(self, root):
		if not root:
			return True
		MAX, MIN = 2 ** 32, -2 ** 32
		return self.helper(root, MAX, MIN)

	def helper(self, root, upper, lower):
		if not root:
			return True
		if root.val >= upper or root.val <= lower:
			return False
		return self.helper(root.left, root.val, lower) and self.helper(root.right, upper, root.val)