import random
from unittest import TestCase

from total_hamming_distance import Solution


class TestTotalHammingDistance(TestCase):
    def test_total_hamming_distance(self):
        # Setup
        sol = Solution()
        nums = [random.randint(1, 1000000) for _ in range(100)]

        # Exercise
        ans = sol.total_hamming_distance(nums)

        # Verify
        expected_ans = self.total_hamming_distance(nums)
        self.assertEqual(ans, expected_ans)

    def total_hamming_distance(self, nums):
        total_dist = 0
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                n, m = nums[i], nums[j]
                total_dist += self.calc_distance(n, m)
        return total_dist

    def calc_distance(self, n, m):
        xor = n ^ m
        dist = 0
        while xor != 0:
            dist += xor & 1
            xor >>= 1
        return dist
