class Solution(object):
    def sum_numbers(self, root):
        self.ans = 0
        self.traverse(root, 0)
        return self.ans

    def traverse(self, root, cur):
        if root is None:
            return
        next_ = 10 * cur + root.val
        if root.left is None and root.right is None:
            self.ans += next_
        if root.left is not None:
            self.traverse(root.left, next_)
        if root.right is not None:
            self.traverse(root.right, next_)
