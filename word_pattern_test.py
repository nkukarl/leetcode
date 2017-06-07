from unittest import TestCase

from nose_parameterized import parameterized

from word_pattern import Solution


class TestWordPattern(TestCase):
    @parameterized.expand([
        [
            {
                'pattern': 'abba',
                'string': 'dog cat cat dog',
            },
            True,
        ],
        [
            {
                'pattern': 'abba',
                'string': 'dog cat cat fish',
            },
            False,
        ],
        [
            {
                'pattern': 'aaaa',
                'string': 'dog cat cat dog',
            },
            False,
        ],
        [
            {
                'pattern': 'abba',
                'string': 'dog dog dog dog',
            },
            False,
        ],
    ])
    def test_word_pattern(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.word_pattern(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
