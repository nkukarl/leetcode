from unittest import TestCase

from nose_parameterized import parameterized

from interleaving_string import Solution


class TestInterleavingString(TestCase):
    @parameterized.expand([
        [
            {
                's1': '',
                's2': '',
                's3': '',
            },
            True,
        ],
        [
            {
                's1': 'a',
                's2': '',
                's3': 'a',
            },
            True,
        ],
        [
            {
                's1': 'abc',
                's2': 'abc',
                's3': 'aabbcc',
            },
            True,
        ],
        [
            {
                's1': 'aabcc',
                's2': 'dbbca',
                's3': 'aadbbcbcac',
            },
            True,
        ],
        [
            {
                's1': 'aabcc',
                's2': 'dbbca',
                's3': 'aadbbbaccc',
            },
            False,
        ],
    ])
    def test_is_interleave(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_interleave(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
