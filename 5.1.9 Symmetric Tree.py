class Solution:
	def isSymmetric(self, root):
		if not root:
			return True
		return self.helper(root.left, root.right)

	def helper(self, L, R):
		if not L and not R:
			return True
		if not L or not R:
			return False
		if L.val != R.val:
			return False
		return self.helper(L.left, R.right) and self.helper(L.right, R.left)