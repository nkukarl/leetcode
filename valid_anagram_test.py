import random
import string
from unittest import TestCase

from valid_anagram import Solution


class TestValidAnagram(TestCase):
    def get_random_seq(self, n):
        return [random.choice(string.ascii_lowercase) for _ in range(n)]

    def test_valid_anagram_true(self):
        # Setup
        sol = Solution()
        base_seq = self.get_random_seq(10)
        s = ''.join(base_seq)
        random.shuffle(base_seq)
        t = ''.join(base_seq)
        # Exercise
        ans = sol.is_anagram(s, t)

        # Verify
        self.assertTrue(ans)

    def test_valid_anagram_false(self):
        # Setup
        sol = Solution()
        s = t = ''
        while True:
            s = ''.join(self.get_random_seq(10))
            t = ''.join(self.get_random_seq(10))
            if s != t:
                break

        # Exercise
        ans = sol.is_anagram(s, t)

        # Verify
        self.assertFalse(ans)
