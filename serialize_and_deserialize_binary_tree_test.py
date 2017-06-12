from unittest import TestCase

from serialize_and_deserialize_binary_tree import Codec
from utils_tree import compare_trees, construct_tree, TreeNode


class TestSerializeAndDeserializeBST(TestCase):
    def test_serialize_complete_tree(self):
        """
                        4
                       / \
                      2   6
                     / \ / \
                    1  3 5  7
        """
        # Setup
        codec = Codec()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        data = codec.serialize(root)

        # Verify
        expected_data = '[[4],[2,6],[1,3,5,7]]'
        self.assertTrue(data, expected_data)

    def test_deserialize_complete_tree(self):
        """
                        4
                       / \
                      2   6
                     / \ / \
                    1  3 5  7
        """
        # Setup
        codec = Codec()
        data = '[[4],[2,6],[1,3,5,7]]'

        # Exercise
        root = codec.deserialize(data)

        # Verify
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        expected_root = construct_tree(serialized_data)
        self.assertTrue(compare_trees(root, expected_root))

    def test_serialize_non_complete_tree(self):
        """
                        4
                       /
                      2
                       \
                        3
        """
        # Setup
        codec = Codec()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)

        # Exercise
        data = codec.serialize(root)

        # Verify
        expected_data = '[[4],[2,None],[None,3]]'
        self.assertTrue(data, expected_data)

    def test_deserialize_non_complete_tree(self):
        """
                        4
                       /
                      2
                       \
                        3
        """
        # Setup
        codec = Codec()
        data = '[[4],[2,None],[None,3]]'

        # Exercise
        root = codec.deserialize(data)

        # Verify
        expected_root = TreeNode(4)
        expected_root.left = TreeNode(2)
        expected_root.left.right = TreeNode(3)
        self.assertTrue(compare_trees(root, expected_root))

    def test_serialize_non_complete_tree_complicated(self):
        """
                        5
                       / \
                      4   7
                     /   /
                    3   2
                   /   /
                  -1  9
        """
        # Setup
        codec = Codec()
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(7)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(2)
        root.left.left.left = TreeNode(-1)
        root.right.left.left = TreeNode(9)

        # Exercise
        data = codec.serialize(root)

        # Verify
        expected_data = '[[5],[4,7],[3,None,2,None],[-1,None,9]]'
        self.assertTrue(data, expected_data)

    def test_deserialize_non_complete_tree_complicated(self):
        """
                        5
                       / \
                      4   7
                     /   /
                    3   2
                   /   /
                  -1  9
        """
        # Setup
        codec = Codec()
        data = '[[5],[4,7],[3,None,2,None],[-1,None,9]]'

        # Exercise
        root = codec.deserialize(data)

        # Verify
        expected_root = TreeNode(5)
        expected_root.left = TreeNode(4)
        expected_root.right = TreeNode(7)
        expected_root.left.left = TreeNode(3)
        expected_root.right.left = TreeNode(2)
        expected_root.left.left.left = TreeNode(-1)
        expected_root.right.left.left = TreeNode(9)
        self.assertTrue(compare_trees(root, expected_root))
