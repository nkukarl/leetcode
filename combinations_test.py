from unittest import TestCase

from combinations import Solution


class TestCombinations(TestCase):
    def test_combine_k_less_than_half_of_n(self):
        # Setup
        sol = Solution()
        n, k = 5, 2

        # Exercise
        ans = sol.combine(n, k)

        # Verify
        expected_ans = [
            [1, 2], [1, 3], [1, 4], [1, 5],
            [2, 3], [2, 4], [2, 5], [3, 4],
            [3, 5], [4, 5]
        ]
        self.assertEqual(sorted(ans), sorted(expected_ans))

    def test_combine_k_greater_than_half_of_n(self):
        # Setup
        sol = Solution()
        n, k = 6, 5

        # Exercise
        ans = sol.combine(n, k)

        # Verify
        expected_ans = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 6],
            [1, 2, 3, 5, 6],
            [1, 2, 4, 5, 6],
            [1, 3, 4, 5, 6],
            [2, 3, 4, 5, 6],
        ]
        self.assertEqual(sorted(ans), sorted(expected_ans))
