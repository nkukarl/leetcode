from utils_tree import TreeNode


class SolutionPreorderInorder(object):
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


class SolutionInorderPostorder(object):
    def build_tree(self, inorder, postorder):
        if 0 == len(inorder) or 0 == len(postorder):
            return None
        root_val = postorder[-1]
        pivot = inorder.index(root_val)
        inorder_left = inorder[:pivot]
        inorder_right = inorder[pivot + 1:]
        postorder_left = postorder[:pivot]
        postorder_right = postorder[pivot: -1]

        root = TreeNode(root_val)
        root.left = self.build_tree(inorder_left, postorder_left)
        root.right = self.build_tree(inorder_right, postorder_right)

        return root
