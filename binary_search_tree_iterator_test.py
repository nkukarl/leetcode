from unittest import TestCase

from binary_search_tree_iterator import BSTIterator
from utils_tree import get_root_tree


class TestBinarySearchTreeIterator(TestCase):
    def test_bst_iterator(self):
        # Setup
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)
        bst_iterator = BSTIterator(root)

        # Exercise and Verify
        for n in tree_raw:
            self.assertTrue(bst_iterator.has_next())
            self.assertEqual(bst_iterator.next(), n)
        self.assertFalse(bst_iterator.has_next())
        self.assertFalse(bst_iterator.has_next())
