class Solution(object):
    def tree_to_str(self, root):
        if root is None:
            return ''
        left_str = self.tree_to_str(root.left)
        right_str = self.tree_to_str(root.right)

        # None
        if '' == left_str == right_str:
            return str(root.val)

        # Only left
        if '' == left_str:
            return str(root.val) + '()(' + right_str + ')'

        # Only right
        if '' == right_str:
            return str(root.val) + '(' + left_str + ')'

        # Both exist
        return str(root.val) + '(' + left_str + ')(' + right_str + ')'