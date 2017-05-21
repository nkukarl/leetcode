import random
from unittest import TestCase

from integer_replacement import Solution


class TestIntegerReplacement(TestCase):
    def test_integer_replacement(self):
        # Setup
        sol = Solution()
        n = random.randint(1, 2 ** 31 - 1)

        # Exercise
        ans = sol.integer_replacement(n)

        # Verify
        expected_ans = self.integer_replacement(n)
        self.assertEqual(ans, expected_ans)

    def integer_replacement(self, n):
        self.DICT = {}
        return self._operate(n)

    def _operate(self, n):
        if 1 == n:
            return 0
        if n not in self.DICT:
            if 0 == n % 2:
                self.DICT[n] = 1 + self._operate(n // 2)
            else:
                self.DICT[n] = \
                    1 + min(self._operate(n + 1), self._operate(n - 1))
        return self.DICT[n]
