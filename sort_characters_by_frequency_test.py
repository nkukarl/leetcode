import random
import string
from unittest import TestCase

from sort_characters_by_frequency import Solution


class TestSortCharactersByFrequency(TestCase):
    def test_frequency_sort(self):
        # Setup
        sol = Solution()
        N = 5
        letters = random.sample(string.ascii_letters, N)
        counts = sorted(random.sample(range(1, 10), N), reverse=True)
        s_raw = []
        for l, c in zip(letters, counts):
            s_raw.extend([l] * c)
        expected_ans = ''.join(s_raw)
        random.shuffle(s_raw)
        s = ''.join(s_raw)

        # Exercise
        ans = sol.frequency_sort(s)

        # Verify
        self.assertEqual(ans, expected_ans)
