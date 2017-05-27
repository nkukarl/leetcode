from unittest import TestCase

from nose_parameterized import parameterized

from repeated_substring_pattern import Solution


class TestRepeatedSubstringPattern(TestCase):
    @parameterized.expand([
        [
            {
                's': 'abcabcabc',
            },
            True,
        ],
        [
            {
                's': 'abababab',
            },
            True,
        ],
        [
            {
                's': 'abcabcabd',
            },
            False,
        ],
        [
            {
                's': 'aba',
            },
            False
        ],
    ])
    def test_repeated_substring_pattern(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.repeated_substring_pattern(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
