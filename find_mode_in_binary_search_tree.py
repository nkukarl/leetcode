class Solution(object):
    def find_mode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.summary = {}
        self.max_count = 0
        ans = []
        self.traverse(root)
        for k, v in self.summary.items():
            if v == self.max_count:
                ans.append(k)
        return ans

    def traverse(self, root):
        if root is None:
            return
        self.summary[root.val] = self.summary.get(root.val, 0) + 1
        self.max_count = max(self.max_count, self.summary[root.val])
        self.traverse(root.left)
        self.traverse(root.right)
