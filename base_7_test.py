import random
from unittest import TestCase

from base_7 import Solution


class TestBase7(TestCase):
    def test_convert_to_base_7(self):
        # Setup
        sol = Solution()
        expected_ans = random.randint(1, 6) * 100 + \
                       random.randint(0, 6) * 10 + \
                       random.randint(0, 6)
        base = 1
        num = 0
        for d in str(expected_ans)[::-1]:
            num += int(d) * base
            base *= 7

        # Exercise
        ans = sol.convert_to_base_7(num)

        # Verify
        self.assertEqual(int(ans), expected_ans)
