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

        # Verify
        self.assertEqual(ans, ex)
