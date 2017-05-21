from unittest import TestCase

from nose_parameterized import parameterized

from integer_to_english_words import Solution


class TestIntegerToEnglishWords(TestCase):
    @parameterized.expand([
        [
            {
                'num': 102,
            },
            'One Hundred Two',
        ],
        [
            {
                'num': 1234567890,
            },
            'One Billion Two Hundred Thirty Four Million '
            'Five Hundred Sixty Seven Thousand Eight Hundred Ninety',
        ],
        [
            {
                'num': 12345,
            },
            'Twelve Thousand Three Hundred Forty Five',
        ],
        [
            {
                'num': 1000,
            },
            'One Thousand',
        ],
        [
            {
                'num': 1000000,
            },
            'One Million',
        ],

    ])
    def test_number_to_words(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.number_to_words(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
