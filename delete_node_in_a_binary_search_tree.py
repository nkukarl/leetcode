class Solution(object):
    def delete_node(self, root, key_):
        if root is None:
            return root
        if root.val == key_:
            if root.left is None:
                return root.right
            node = self.get_rightmost(root.left)
            node.right = root.right
            return root.left
        if root.val < key_:
            root.right = self.delete_node(root.right, key_)
        else:
            root.left = self.delete_node(root.left, key_)
        return root

    def get_rightmost(self, node):
        while node is not None:
            node = node.right
        return node
