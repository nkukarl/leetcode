from unittest import TestCase

from nose_parameterized import parameterized

from construct_binary_tree_from_traversal import \
    SolutionPreorderInorder, SolutionInorderPostorder
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
        sol = SolutionPreorderInorder()

        # Exercise
        root = sol.build_tree(**kwargs)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))


class TestConstructBinaryTreeFromInorderAndPostorderTraversal(TestCase):
    @parameterized.expand([
        [
            {
                'inorder': [1, 2, 3, 4, 5, 6, 7],
                'postorder': [1, 3, 2, 5, 7, 6, 4],
            },
            get_root_tree([1, 2, 3, 4, 5, 6, 7]),
        ],
    ])
    def test_build_tree(self, kwargs, expected_root):
        # Setup
        sol = SolutionInorderPostorder()

        # Exercise
        root = sol.build_tree(**kwargs)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
