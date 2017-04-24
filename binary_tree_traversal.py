class Solution(object):
    def preorder_traversal(self, root):
        nodes = []
        self._preorder_traversal(root, nodes)
        return nodes

    def _preorder_traversal(self, root, nodes):
        if root is not None:
            nodes.append(root.val)
            self._preorder_traversal(root.left, nodes)
            self._preorder_traversal(root.right, nodes)

    def inorder_traversal(self, root):
        nodes = []
        self._inorder_traversal(root, nodes)
        return nodes

    def _inorder_traversal(self, root, nodes):
        if root is not None:
            self._inorder_traversal(root.left, nodes)
            nodes.append(root.val)
            self._inorder_traversal(root.right, nodes)

    def postorder_traversal(self, root):
        nodes = []
        self._postorder_traversal(root, nodes)
        return nodes

    def _postorder_traversal(self, root, nodes):
        if root is not None:
            self._postorder_traversal(root.left, nodes)
            self._postorder_traversal(root.right, nodes)
            nodes.append(root.val)
