import re
from unittest import TestCase

from keyboard_row import Solution


class TestKeyboardRow(TestCase):
    def find_words_using_regex(self, words):
        ans = []
        for word in words:
            if re.match(r'\b[qwertyuiop]+\b', word, re.I) is not None \
                    or re.match(r'\b[asdfghjkl]+\b', word, re.I) is not None \
                    or re.match(r'\b[zxcvbnm]+\b', word, re.I) is not None:
                ans.append(word)
        return ans

    def test_find_words(self):
        # Setup
        sol = Solution()
        words = ['Hello', 'Alaska', 'Dad', 'Peace']

        # Exercise
        ans = sol.find_words(words)
        expected_ans = self.find_words_using_regex(words)

        # Verify
        self.assertEqual(ans, expected_ans)
