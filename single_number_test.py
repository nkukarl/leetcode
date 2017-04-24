import random
from unittest import TestCase

from single_number import Solution


class TestSingleNumber(TestCase):
    def test_single_number_i(self):
        # Setup
        sol = Solution()
        unique_number = random.randint(1, 9)
        numbers = [x for x in range(1, 10)] * 2 + [unique_number]
        random.shuffle(numbers)

        # Exercise
        ans = sol.single_number_i(numbers)

        # Verify
        self.assertEqual(ans, unique_number)

    def test_single_number_iii(self):
        # Setup
        sol = Solution()
        M = random.randint(3, 10)
        N = random.randint(10, 20)
        unique_number = random.sample(range(1, M), 2)
        numbers = [x for x in range(M, N)] * 2 + unique_number
        random.shuffle(numbers)

        # Exercise
        ans = sol.single_number_iii(numbers)

        # Verify
        self.assertEqual(sorted(ans), sorted(unique_number))
