class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def hasPathSum(self, root, SUM):
        self.SUM = SUM
        self.ans = False
        self.helper(root, [])

        return self.ans

    def helper(self, root, cur):
        if not root:
            if sum(cur) == self.SUM:
                self.ans = True
                return
        else:
            self.helper(root.left, cur + [root.val])
            self.helper(root.right, cur + [root.val])


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

SUM = 22

inst = Solution()
print(inst.hasPathSum(root, SUM))
