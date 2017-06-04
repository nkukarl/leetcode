from utils_tree import TreeNode


class Codec(object):
    def serialize(self, root):
        self.ans = []
        self.traverse(root, 0)
        return str(self.ans[:-1]).replace(' ', '')

    def traverse(self, root, level):
        if len(self.ans) <= level:
            self.ans.append([])
        if root is None:
            self.ans[level].append(None)
        else:
            self.ans[level].append(root.val)
            self.traverse(root.left, level + 1)
            self.traverse(root.right, level + 1)

    def deserialize(self, data):
        # Handle simple scenario
        if len(data) < 4:
            return None

        rows_raw = data[2:-2].split('],[')
        root = TreeNode(int(rows_raw[0]))
        prev = [root]
        for row_raw in rows_raw[1:]:
            row = row_raw.split(',')
            nodes, cur = [], []
            for el in row:
                if el != 'None':
                    node = TreeNode(int(el))
                    cur.append(node)
                else:
                    node = None
                nodes.append(node)
            prev = prev[::-1]
            nodes = nodes[::-1]
            while prev:
                parent = prev.pop()
                parent.left = nodes.pop()
                if nodes:
                    parent.right = nodes.pop()
            prev = cur
        return root