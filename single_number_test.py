import random
from unittest import TestCase

from single_number import Solution


class TestSingleNumber(TestCase):
    def test_single_number(self):
        # Setup
        sol = Solution()
        unique_number = random.randint(1, 9)
        numbers = [x for x in range(1, 10)] * 2 + [unique_number]
        random.shuffle(numbers)

        # Exercise
        ans = sol.single_number(numbers)

        # Verify
        self.assertEqual(ans, unique_number)
