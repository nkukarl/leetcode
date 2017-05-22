from unittest import TestCase

from nose_parameterized import parameterized

from maximal_rectangle import Solution


class TestMaximalRectangle(TestCase):
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
            6,
        ],
    ])
    def test_maximal_rectangle(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.maximal_rectangle(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
