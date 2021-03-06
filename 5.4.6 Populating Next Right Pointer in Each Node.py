class TreeLinkNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.next = None


class Solution:
    def connect(self, root):
        node = root
        while node:
            tmp = None
            cur = None
            while node:
                if not tmp:
                    if node.left:
                        tmp = node.left
                    elif node.right:
                        tmp = node.right
                if node.left:
                    if cur:
                        cur.next = node.left
                    cur = node.left
                if node.right:
                    if cur:
                        cur.next = node.right
                    cur = node.right
                node = node.next
            node = tmp


root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

inst = Solution()
inst.connect(root)
