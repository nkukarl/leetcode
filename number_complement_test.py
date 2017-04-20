import random
from unittest import TestCase

from number_complement import Solution


class TestNumberComplement(TestCase):
    def test_find_complement(self):
        # Setup
        sol = Solution()
        num = random.randint(1, 1000)

        # Exercise
        ans = sol.find_complement(num)

        # Verify
        expected_ans_raw = ''
        for char in bin(num)[2:]:
            expected_ans_raw += '0' if char != '0' else '1'
        expected_ans = int(expected_ans_raw, 2)

        self.assertEqual(ans, expected_ans)
