class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        L = self.getHeight(root.left)
        R = self.getHeight(root.right)
        if abs(L - R) > 1:
            return False
        return self.isBalanced(L.left, L.right) and self.isBalanced(R.left,
                                                                    R.right)

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
