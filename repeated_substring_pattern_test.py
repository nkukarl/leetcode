from unittest import TestCase

from nose_parameterized import parameterized

from repeated_substring_pattern import Solution


class TestRepeatedSubstringPattern(TestCase):
    @parameterized.expand([
        [
            {
                's': '',
            },
        ],
        [
            {
                's': 'a',
            },
        ],
        [
            {
                's': 'abcabcabc',
            },
        ],
        [
            {
                's': 'abababab',
            },
        ],
        [
            {
                's': 'abcabcabd',
            },
        ],
        [
            {
                's': 'aba',
            },
        ],

    ])
    def test_repeated_substring_pattern(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.repeated_substring_pattern(**kwargs)

        # Verify
        expected_ans = self.repeated_substring_pattern(**kwargs)
        self.assertEqual(ans, expected_ans)

    def repeated_substring_pattern(self, s):
        return s != '' and s in (s * 2)[1:-1]
