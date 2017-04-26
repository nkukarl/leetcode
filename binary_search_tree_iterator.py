class BSTIterator(object):
    def __init__(self, root):
        self.nodes = []
        self.pump(root)

    def pump(self, node):
        while node is not None:
            self.nodes.append(node)
            node = node.left

    def has_next(self):
        return len(self.nodes) > 0

    def next(self):
        node = self.nodes.pop()
        self.pump(node.right)
        return node.val
