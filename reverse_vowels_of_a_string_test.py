from unittest import TestCase

from nose_parameterized import parameterized

from reverse_vowels_of_a_string import Solution


class TestReverseVowelsOfAString(TestCase):
    @parameterized.expand([
        [
            {
                's': 'hello',
            },
            'holle',
        ],
        [
            {
                's': 'leetcode',
            },
            'leotcede',
        ],
        [
            {
                's': '1a1e1i1o1u1',
            },
            '1u1o1i1e1a1',
        ],
    ])
    def test_reverse_vowels(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.reverse_vowels(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
