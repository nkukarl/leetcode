class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def sortedArrayToBST(self, A):
        if not A:
            return None
        mid = len(A) // 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root


A = [1, 2, 3, 4, 5, 6, 7]

inst = Solution()
inst.sortedArrayToBST(A)
