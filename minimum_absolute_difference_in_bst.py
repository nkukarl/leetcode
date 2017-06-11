class Solution(object):
    def get_minimum_difference(self, root):
        self.nodes = []
        self.push_left(root)

        min_diff = prev = None
        while self.nodes:
            node = self.nodes.pop()
            self.push_left(node.right)
            if prev is None:
                prev = node.val
                continue
            diff = node.val - prev
            if min_diff is None:
                min_diff = diff
            else:
                min_diff = min(min_diff, diff)
            prev = node.val

        return min_diff

    def push_left(self, root):
        while root:
            self.nodes.append(root)
            root = root.left

    def get_minimum_difference_inorder_traverse(self, root):
        nums = []
        self.traverse(root, nums)
        return min([n1 - n2 for n1, n2 in zip(nums[1:], nums[:-1])])

    def traverse(self, root, nums):
        if root is None:
            return
        self.traverse(root.left, nums)
        nums.append(root.val)
        self.traverse(root.right, nums)
