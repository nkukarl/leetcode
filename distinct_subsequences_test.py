from unittest import TestCase

from nose_parameterized import parameterized

from distinct_subsequences import Solution


class TestDistinctSubsequences(TestCase):
    @parameterized.expand([
        [
            {
                's': 'rabbbit',
                't': 'rabbit',
            },
            3,
        ],
        [
            {
                's': 'abcde',
                't': 'ace',
            },
            1,
        ],
    ])
    def test_num_distinct(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.num_distinct(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
