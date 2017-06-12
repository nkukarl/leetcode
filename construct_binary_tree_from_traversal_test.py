from unittest import TestCase

from nose_parameterized import parameterized

from construct_binary_tree_from_traversal import \
    SolutionPreorderInorder, SolutionInorderPostorder
from utils_tree import compare_trees, construct_tree


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(TestCase):
    @parameterized.expand([
        [
            {
                'preorder': [4, 2, 1, 3, 6, 5, 7],
                'inorder': [1, 2, 3, 4, 5, 6, 7],
            },
            construct_tree([[4], [2, 6], [1, 3, 5, 7]]),
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
            construct_tree([[4], [2, 6], [1, 3, 5, 7]]),
        ],
    ])
    def test_build_tree(self, kwargs, expected_root):
        # Setup
        sol = SolutionInorderPostorder()

        # Exercise
        root = sol.build_tree(**kwargs)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
