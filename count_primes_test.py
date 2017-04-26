import random
from unittest import TestCase

from count_primes import Solution


class TestCountPrimes(TestCase):
    def test_count_primes(self):
        # Setup
        sol = Solution()
        n = random.randint(20, 50)

        # Exercise
        ans = sol.count_primes(n)

        # Verify
        expected_ans = self.count_primes(n)
        self.assertEqual(ans, expected_ans)

    def count_primes(self, n):
        count = 0
        for m in range(2, n):
            if self.is_prime(m):
                count += 1
        return count

    def is_prime(self, n):
        for m in range(2, int(n ** 0.5) + 1):
            if 0 == n % m:
                return False
        return True
