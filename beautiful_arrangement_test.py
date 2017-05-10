from unittest import TestCase

from beautiful_arrangement import Solution

COUNT = \
    [0, 1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679]


class TestCountArrangement(TestCase):
    def test_count_arrangement(self):
        # Setup
        sol = Solution()

        # Exercise and Verify
        for n in range(1, 16):
            ans = sol.count_arrangement(n)
            expected_ans = COUNT[n]
            self.assertEqual(ans, expected_ans)
