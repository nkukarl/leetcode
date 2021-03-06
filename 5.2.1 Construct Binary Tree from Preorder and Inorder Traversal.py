class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        pos = inorder.index(val)
        preLeft = preorder[1: pos + 1]
        preRight = preorder[pos + 1:]
        inLeft = inorder[:pos]
        inRight = inorder[pos + 1:]
        root.left = self.buildTree(preLeft, inLeft)
        root.right = self.buildTree(preRight, inRight)
        return root


preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]

inst = Solution()
root = inst.buildTree(preorder, inorder)
