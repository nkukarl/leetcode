from unittest import TestCase

from nose_parameterized import parameterized

from word_search_ii import Solution

BOARD = [
    'ABCE',
    'SFCS',
    'ADEE',
]


class TestWordSearchII(TestCase):
    @parameterized.expand([
        [
            {
                'board': BOARD,
                'words': [
                    'ABCCED', 'SEE', 'ABCB', 'ABCESEEDASFC',
                ],
            },
            ['ABCCED', 'SEE', 'ABCESEEDASFC'],
        ],
    ])
    def test_find_words(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_words(**kwargs)

        # Verify
        self.assertEqual(set(ans), set(expected_ans))
