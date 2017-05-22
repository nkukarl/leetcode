from unittest import TestCase

from nose_parameterized import parameterized

from maximal_square import Solution


class TestMaximalSquare(TestCase):
    @parameterized.expand([
        [
            {
                'matrix': [
                    '10100',
                    '10111',
                    '11111',
                    '10010',
                ]
            },
            4,
        ],
    ])
    def test_maximal_square(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.maximal_square(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
