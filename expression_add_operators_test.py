from unittest import TestCase

from nose_parameterized import parameterized

from expression_add_operators import Solution


class TestExpressAddOperator(TestCase):
    @parameterized.expand([
        [
            {
                'num': '12345',
                'target': -1,
            },
            ['1+2-3+4-5'],
        ],
        [
            {
                'num': '123',
                'target': 6,
            },
            ['1+2+3', '1*2*3'],
        ],
        [
            {
                'num': '232',
                'target': 8,
            },
            ['2*3+2', '2+3*2'],
        ],
        [
            {
                'num': '105',
                'target': 5,
            },
            ['1*0+5', '10-5'],
        ],
        [
            {
                'num': '00',
                'target': 0,
            },
            ['0+0', '0*0', '0-0'],
        ],
    ])
    def test_add_operators(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.add_operators(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
