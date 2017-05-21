from unittest import TestCase

from nose_parameterized import parameterized

from word_search import Solution

BOARD = [
    'ABCE',
    'SFCS',
    'ADEE',
]


class TestWordSearch(TestCase):
    @parameterized.expand([
        [
            {
                'board': BOARD,
                'word': 'ABCCED',
            },
            True,
        ],
        [
            {
                'board': BOARD,
                'word': 'SEE',
            },
            True,
        ],
        [
            {
                'board': BOARD,
                'word': 'ABCB',
            },
            False,
        ],
        [
            {
                'board': BOARD,
                'word': 'ABCESEEDASFC',
            },
            True,
        ],
        [
            {
                'board': ['A'],
                'word': 'A',
            },
            True,
        ],

    ])
    def test_exist(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.exist(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
