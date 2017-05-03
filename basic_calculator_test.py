from unittest import TestCase

from nose_parameterized import parameterized

from basic_calculator import Solution


class TestBasicCalculator(TestCase):
    @parameterized.expand([
        [
            {
                's': '1 + 1',
            },
        ],
        [
            {
                's': ' 22-135 + 12 - 23 ',
            },
        ],
        [
            {
                's': '(11+(344+345+12)-203)+(16+18)',
            },
        ],
        [
            {
                's': '-1',
            }
        ]

    ])
    def test_calculate(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.calculate(**kwargs)
        expected_ans = eval(kwargs['s'])

        # Verify
        self.assertEqual(ans, expected_ans)

    @parameterized.expand([
        [
            {
                'ss': ['1', '+', '1'],
            },
            2,
        ],
        [
            {
                'ss': ['2', '-', '1', '+', '2'],
            },
            3,
        ],
        [
            {
                'ss': ['1', '+', '2', '-', '3', '+', '4', '-', '5'],
            },
            -1,
        ],

    ])
    def test_calc(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol._calc(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
