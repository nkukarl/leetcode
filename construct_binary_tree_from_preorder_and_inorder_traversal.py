from utils_tree import TreeNode


class Solution(object):
    def build_tree(self, preorder, inorder):
        if 0 == len(preorder) or 0 == len(inorder):
            return None
        root_val = preorder[0]
        pivot = inorder.index(root_val)
        preorder_left = preorder[1:pivot + 1]
        preorder_right = preorder[pivot + 1:]
        inorder_left = inorder[:pivot]
        inorder_right = inorder[pivot + 1:]

        root = TreeNode(root_val)
        root.left = self.build_tree(preorder_left, inorder_left)
        root.right = self.build_tree(preorder_right, inorder_right)

        return root
