from unittest import TestCase

from nose_parameterized import parameterized

from construct_binary_tree_from_preorder_and_inorder_traversal import Solution
from utils_tree import get_root_tree, compare_trees


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(TestCase):
    @parameterized.expand([
        [
            {
                'preorder': [4, 2, 1, 3, 6, 5, 7],
                'inorder': [1, 2, 3, 4, 5, 6, 7],
            },
            get_root_tree([1, 2, 3, 4, 5, 6, 7]),
        ],
    ])
    def test_build_tree(self, kwargs, expected_root):
        # Setup
        sol = Solution()

        # Exercise
        root = sol.build_tree(**kwargs)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
