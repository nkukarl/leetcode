from unittest import TestCase

from nose_parameterized import parameterized

from longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters(TestCase):
    @parameterized.expand([
        [
            {
                's': '',
            },
            0,
        ],
        [
            {
                's': 'a',
            },
            1,
        ],
        [
            {
                's': 'abcabcbb',
            },
            3,
        ],
        [
            {
                's': 'bbbbb',
            },
            1,
        ],
        [
            {
                's': 'pwwkew',
            },
            3,
        ],
    ])
    def test_length_of_longest_substring(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.length_of_longest_substring(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
