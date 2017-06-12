from unittest import TestCase

from nose_parameterized import parameterized

from design_compressed_string_iterator import StringIterator


class TestDesignCompressedStringIterator(TestCase):
    @parameterized.expand([
        [
            {
                'compressed_string': 'x6',
            },
            'xxxxxx',
        ],
        [
            {
                'compressed_string': 'L1e2t1C1o1d1e1',
            },
            'LeetCode',
        ],
    ])
    def test_string_iterator(self, kwargs, uncompressed_string):
        # Setup
        string_iterator = StringIterator(**kwargs)

        # Exercise and Verify
        for char in uncompressed_string:
            self.assertTrue(string_iterator.has_next())
            self.assertEqual(string_iterator.next(), char)

        for _ in range(10):
            self.assertFalse(string_iterator.has_next())
            self.assertEqual(string_iterator.next(), ' ')
