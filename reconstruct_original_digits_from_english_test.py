import random
from unittest import TestCase

from reconstruct_original_digits_from_english import Solution


class TestReconstructOriginalDigitsFromEnglish(TestCase):
    def test_original_digits(self):
        # Setup
        sol = Solution()
        num = random.randint(1, 1000000)
        s = self.get_shuffled_english(num)

        # Exercise
        ans = sol.original_digits(s)

        # Verify
        expected_ans = ''.join(sorted(list(str(num))))
        self.assertEqual(ans, expected_ans)

    def get_shuffled_english(self, num):
        D = {
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
        }
        english = []
        for char in str(num):
            english.extend(list(D[char]))
        random.shuffle(english)
        return ''.join(english)
