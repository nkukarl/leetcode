class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_root_tree(tree_raw):
    """

    This method takes a list of integers builds a binary tree.
    E.g.,
    tree_raw = [1, 2, 3, 4, 5, 6, 7]
    tree:

            4
           / \
          /   \
         2     6
        / \   / \
       /   \ /   \
      1    3 5    7

    tree_raw = [None, 2, 3, 4, None, 6, 7]
    tree:

            4
           / \
          /   \
         2     6
        / \   / \
       /   \ /   \
           3      7

    Args:
        tree_raw (List):

    Returns:
        root

    """
    length = len(tree_raw)
    if 0 == length:
        return None
    if 1 == length:
        if tree_raw[0] is None:
            return None
        return TreeNode(tree_raw[0])

    root = TreeNode(tree_raw[length // 2])
    left_tree_raw = tree_raw[:length // 2]
    right_tree_raw = tree_raw[length // 2 + 1:]
    root.left = get_root_tree(left_tree_raw)
    root.right = get_root_tree(right_tree_raw)

    return root


def compare_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.val != root2.val:
        return False
    return compare_trees(root1.left, root2.left) and \
           compare_trees(root1.right, root2.right)


def construct_tree(serialized_data):
    """
    E.g., Tree
                    5
                   / \
                  4   7
                 /   /
                3   2
               /   /
              -1  9
    can be specified as 
    serialized_data = [[5], [4, 7], [3, None, 2, None], [-1, None, 9]]
    """

    if 0 == len(serialized_data):
        return None
    root = TreeNode(serialized_data[0][0])
    prev = [root]
    for row in serialized_data[1:]:
        nodes, cur = [], []
        for el in row:
            if el is not None:
                node = TreeNode(el)
                cur.append(node)
            else:
                node = None
            nodes.append(node)
        prev = prev[::-1]
        nodes = nodes[::-1]
        while prev and nodes:
            parent = prev.pop()
            parent.left = nodes.pop()
            if nodes:
                parent.right = nodes.pop()
        prev = cur
    return root
