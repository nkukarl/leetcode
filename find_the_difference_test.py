import random
import string
from unittest import TestCase

from find_the_difference import Solution


class TestFindTheDifference(TestCase):
    def test_find_the_difference(self):
        # Setup
        sol = Solution()
        N = random.randint(5, 20)
        chars = string.ascii_lowercase
        s_raw = [random.choice(chars) for _ in range(N)]
        s = ''.join(s_raw)
        ex = random.choice(chars)
        t_raw = s_raw + [ex]
        random.shuffle(t_raw)
        t = ''.join(t_raw)

        # Exercise
        ans = sol.find_the_difference(s, t)
        ans_xor = sol.find_the_difference_xor(s, t)

        # Verify
        self.assertEqual(ans, ex)
        self.assertEqual(ans_xor, ex)

    def find_the_difference(self, s, t):
        summary_s = self.summarise(s)
        summary_t = self.summarise(t)
        for c, n in summary_t.items():
            if n != summary_s.get(c, 0):
                return c

    def summarise(self, s):
        summary = {}
        for c in s:
            summary[c] = summary.get(c, 0) + 1
        return summary
