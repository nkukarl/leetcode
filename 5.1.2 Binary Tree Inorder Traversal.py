class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def inorderTraversal(self, root):
        self.res = []
        self.helper(root)

        return self.res

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.res.append(root.val)
            self.helper(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

inst = Solution()
print(inst.inorderTraversal(root))
