from unittest import TestCase

from nose_parameterized import parameterized

from is_subsequence import Solution


class TestIsSubsequence(TestCase):
    @parameterized.expand([
        [
            {
                's': 'abc',
                't': 'ahbgdc',
            },
            True,
        ],
        [
            {
                's': 'axc',
                't': 'ahbgdc',
            },
            False,
        ],
        [
            {
                's': 'abc',
                't': 'axxcxxb',
            },
            False,
        ],
    ])
    def test_is_subsequence(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_subsequence(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
