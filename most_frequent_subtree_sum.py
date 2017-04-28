class Solution(object):
    def find_frequent_tree_sum(self, root):
        if root is None:
            return []
        self.summary = {}
        self.count_max = 0
        self.get_sum(root)
        ans = []
        for k, v in self.summary.items():
            if v == self.count_max:
                ans.append(k)
        return ans

    def get_sum(self, root):
        if root is None:
            return 0
        sum_left = self.get_sum(root.left)
        sum_right = self.get_sum(root.right)
        total = sum_left + sum_right + root.val
        self.summary[total] = self.summary.get(total, 0) + 1
        self.count_max = max(self.count_max, self.summary[total])
        return total
