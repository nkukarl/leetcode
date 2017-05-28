from unittest import TestCase

from nose_parameterized import parameterized

from fraction_addition_and_subtraction import Solution


class TestFractionAdditionAndSubtraction(TestCase):
    @parameterized.expand([
        [
            {
                'expression': '1/2+3/4+6/5',
            },
            '49/20',
        ],
        [
            {
                'expression': '1/2+1/2',
            },
            '1/1',
        ],
    ])
    def test_fraction_addition(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.fraction_addition(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
