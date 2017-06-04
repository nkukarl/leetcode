from unittest import TestCase

from serialize_and_deserialize_bst import Codec
from utils_tree import construct_tree


class TestSerializeAndDeserializeBST(TestCase):
    def test_deserialize_complete_tree(self):
        # Setup
        codec = Codec()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        preorder, inorder = codec.serialize(root)

        # Verify
        expected_preorder = [4, 2, 1, 3, 6, 5, 7]
        expected_inorder = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(preorder, expected_preorder)
        self.assertEqual(inorder, expected_inorder)

    def test_deserialize_non_complete_tree(self):
        # Setup
        codec = Codec()
        serialized_data = [[4], [2, 6], [None, 3, 5]]
        root = construct_tree(serialized_data)

        # Exercise
        preorder, inorder = codec.serialize(root)

        # Verify
        expected_preorder = [4, 2, 3, 6, 5]
        expected_inorder = [2, 3, 4, 5, 6]
        self.assertEqual(preorder, expected_preorder)
        self.assertEqual(inorder, expected_inorder)

    def test_deserialize_non_complete_tree_complicated(self):
        # Setup
        codec = Codec()
        serialized_data = [[20], [10, 30], [5, None, 25], [3, None, None, 27]]
        root = construct_tree(serialized_data)

        # Exercise
        preorder, inorder = codec.serialize(root)

        # Verify
        expected_preorder = [20, 10, 5, 3, 30, 25, 27]
        expected_inorder = [3, 5, 10, 20, 25, 27, 30]
        self.assertEqual(preorder, expected_preorder)
        self.assertEqual(inorder, expected_inorder)
