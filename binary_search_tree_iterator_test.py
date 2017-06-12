from unittest import TestCase

from binary_search_tree_iterator import BSTIterator
from utils_tree import construct_tree


class TestBinarySearchTreeIterator(TestCase):
    def test_bst_iterator(self):
        # Setup
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)
        bst_iterator = BSTIterator(root)

        # Exercise and Verify
        for n in [1, 2, 3, 4, 5, 6, 7]:
            self.assertTrue(bst_iterator.has_next())
            self.assertEqual(bst_iterator.next(), n)
        self.assertFalse(bst_iterator.has_next())
        self.assertFalse(bst_iterator.has_next())
