from unittest import TestCase

from implement_trie import Trie


class TestTrie(TestCase):
    def test_trie(self):
        # Setup
        trie = Trie()

        # Exercise and Verify

        self.assertFalse(trie.starts_with('b'))

        trie.insert('but')
        trie.insert('butter')
        trie.insert('bad')
        trie.insert('bat')

        self.assertFalse(trie.search('bu'))
        self.assertTrue(trie.search('but'))
        self.assertFalse(trie.search('butt'))
        self.assertTrue(trie.search('butter'))
        self.assertTrue(trie.search('bad'))

        self.assertTrue(trie.starts_with('bu'))
        self.assertFalse(trie.starts_with('da'))
        self.assertFalse(trie.starts_with('ab'))
