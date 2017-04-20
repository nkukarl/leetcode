import random
from unittest import TestCase

from hamming_distance import Solution


class TestHammingDistance(TestCase):
    def calculate_distance(self, num1, num2):
        num1 = bin(num1)[2:]
        num2 = bin(num2)[2:]
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 = (len(num1) - len(num2)) * '0' + num2
        distance = 0
        for b1, b2 in zip(num1, num2):
            distance += b1 != b2
        return distance

    def test_hamming_distance(self):
        # Setup
        sol = Solution()
        num1 = random.randint(1, 2 ** 31 - 1)
        num2 = random.randint(1, 2 ** 31 - 1)

        # Exercise
        ans = sol.hamming_distance(num1, num2)

        # Verify
        expected_ans = self.calculate_distance(num1, num2)
        self.assertEqual(ans, expected_ans)
