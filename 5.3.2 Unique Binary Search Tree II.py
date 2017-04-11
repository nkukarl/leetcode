class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def generate(self, n):
        if not n:
            return []
        return self.helper(1, n + 1)

    def helper(self, left, right):
        if left >= right:
            return [None]
        res = []
        for n in range(left, right):
            ls = self.helper(left, n)
            rs = self.helper(n + 1, right)
            for l in ls:
                for r in rs:
                    root = TreeNode(n)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


inst = Solution()
inst.generate(1)
