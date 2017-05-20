from unittest import TestCase

from add_and_search_word import WordDictionary


class TestAddAndSearchWord(TestCase):
    def test_word_dictionary(self):
        # Setup
        word_dictionary = WordDictionary()

        # Exercise and Verify

        self.assertFalse(word_dictionary.search('t'))

        word_dictionary.add_word('apple')
        word_dictionary.add_word('tea')
        word_dictionary.add_word('water')
        word_dictionary.add_word('pen')
        word_dictionary.add_word('pencil')

        self.assertTrue(word_dictionary.search('apple'))
        self.assertTrue(word_dictionary.search('a..le'))
        self.assertTrue(word_dictionary.search('tea'))
        self.assertFalse(word_dictionary.search('t'))
        self.assertTrue(word_dictionary.search('w.t.r'))
        self.assertTrue(word_dictionary.search('pen'))
        self.assertFalse(word_dictionary.search('penc'))
        self.assertTrue(word_dictionary.search('pencil'))
