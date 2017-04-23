import random
from unittest import TestCase

from counting_bits import Solution


class TestCountingBits(TestCase):
    def test_count_bits(self):
        # Setup
        sol = Solution()
        num = random.randint(20, 30)

        # Exercise
        ans = sol.count_bits(num)
        expected_ans = self.count_bits(num)

        # Verify
        self.assertEqual(ans, expected_ans)

    def count_bits(self, num):
        bits = []
        for n in range(num + 1):
            bit = 0
            while n > 0:
                bit += n & 1
                n >>= 1
            bits.append(bit)
        return bits

