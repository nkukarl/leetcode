from unittest import TestCase

from binary_tree_traversal import Solution
from utils_tree import construct_tree


class TestBinaryTreeTraversal(TestCase):
    def setup(self):
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)
        return root

    def test_preorder_traversal(self):
        # Setup
        sol = Solution()
        root = self.setup()

        # Exercise
        ans = sol.preorder_traversal(root)

        # Verify
        expected_ans = [4, 2, 1, 3, 6, 5, 7]
        self.assertEqual(ans, expected_ans)

    def test_inorder_traversal(self):
        # Setup
        sol = Solution()
        root = self.setup()

        # Exercise
        ans = sol.inorder_traversal(root)

        # Verify
        expected_ans = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(ans, expected_ans)

    def test_postorder_traversal(self):
        # Setup
        sol = Solution()
        root = self.setup()

        # Exercise
        ans = sol.postorder_traversal(root)

        # Verify
        expected_ans = [1, 3, 2, 5, 7, 6, 4]
        self.assertEqual(ans, expected_ans)
