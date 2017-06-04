from unittest import TestCase

from nose_parameterized import parameterized

from word_break import Solution


class TestWordBreak(TestCase):
    @parameterized.expand([
        [
            {
                's': 'leetcode',
                'word_dict': ['leet', 'code'],
            },
            True,
        ],
        [
            {
                's': 'leetcode',
                'word_dict': ['leek', 'et', 'code'],
            },
            False,
        ],
    ])
    def test_word_break(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.word_break(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
