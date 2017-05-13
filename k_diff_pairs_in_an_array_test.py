from unittest import TestCase

from nose_parameterized import parameterized

from k_diff_pairs_in_an_array import Solution


class TestKDiffPairsInAnArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [3, 1, 4, 1, 5],
                'k': 2,
            },
            2,
        ],
        [
            {
                'nums': [1, 3, 1, 5, 4],
                'k': 0,
            },
            1,
        ],
        [
            {
                'nums': [1, 2, 3, 4, 5],
                'k': 1,
            },
            4
        ],
    ])
    def test_find_pairs(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_pairs(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
