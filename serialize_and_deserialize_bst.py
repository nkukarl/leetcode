from utils_tree import TreeNode

class Codec(object):
    def serialize(self, root):
        preorder, inorder = [], []
        self.preorder_traverse(root, preorder)
        self.inorder_traverse(root, inorder)
        return preorder, inorder

    def preorder_traverse(self, root, cur):
        if root is not None:
            cur.append(root.val)
            self.preorder_traverse(root.left, cur)
            self.preorder_traverse(root.right, cur)

    def inorder_traverse(self, root, cur):
        if root is not None:
            self.inorder_traverse(root.left, cur)
            cur.append(root.val)
            self.inorder_traverse(root.right, cur)

    def deserialize(self, data):
        preorder, inorder = data
        return self.build(preorder, inorder)

    def build(self, preorder, inorder):
        if 0 == len(preorder) * len(inorder):
            return None
        root_val = preorder[0]
        pos = inorder.index(root_val)
        pre_left = preorder[1: pos + 1]
        pre_right = preorder[pos + 1:]
        in_left = inorder[:pos]
        in_right = inorder[pos + 1:]

        root = TreeNode(root_val)
        root.left = self.build(pre_left, in_left)
        root.right = self.build(pre_right, in_right)
        return root