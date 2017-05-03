from unittest import TestCase

from nose_parameterized import parameterized

from evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(TestCase):
    @parameterized.expand([
        [
            {
                'tokens': ['4', '13', '5', '/', '+']
            },
            6,
        ],
        [
            {
                'tokens': ['2', '1', '+', '3', '*']
            },
            9,
        ],
        [
            {
                'tokens': [
                    '10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+',
                    '5', '+',
                ]
            },
            22,
        ]
    ])
    def test_eval_rpn(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.eval_rpn(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
