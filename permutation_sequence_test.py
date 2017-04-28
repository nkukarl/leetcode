import random
from unittest import TestCase

from permutation_sequence import Solution


class TestPermutationSequence(TestCase):
    def test_get_permutation(self):
        # Setup
        sol = Solution()
        n = random.randint(1, 9)
        k = sol.get_factorial()[n]

        # Exercise
        ans = sol.get_permutation(n, k)
        expected_ans = self.get_permutation(n, k)

        # Verify
        self.assertEqual(ans, expected_ans)

    def test_get_factorial(self):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_factorial()
        expected_ans = [
            1,  # 0!
            1,  # 1!
            2,  # 2!
            6,  # 3!
            24,
            120,
            720,
            5040,
            40320,
            362880,
        ]

        # Verify
        self.assertEqual(ans, expected_ans)

    def get_permutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        self.permutations = []
        self.build(nums, '')
        # self.permutations.sort()
        return self.permutations[k - 1]

    def build(self, nums, cur):
        if 0 == len(nums):
            self.permutations.append(cur)
        else:
            for i, n in enumerate(nums):
                self.build(nums[:i] + nums[i + 1:], cur + nums[i])
