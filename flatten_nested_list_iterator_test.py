from unittest import TestCase

from flatten_nested_list_iterator import NestedIteratorSelf


class TestNestedIteratorSelf(TestCase):
    def test_nested_iterator_self(self):
        # Setup
        nested_list = [[0, 1, 2], [3, [4, 5]], [6]]
        sol = NestedIteratorSelf(nested_list)

        # Exercise and Verify
        for n in range(7):
            self.assertTrue(sol.has_next())
            self.assertEqual(sol.next(), n)
        self.assertFalse(sol.has_next())
        self.assertFalse(sol.has_next())
