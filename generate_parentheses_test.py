from unittest import TestCase

from nose_parameterized import parameterized

from generate_parentheses import Solution


class TestGenerateParentheses(TestCase):
    @parameterized.expand([
        [
            {
                'n': 3,
            },
            [
                '()()()', '()(())', '(())()', '(()())', '((()))',
            ],
        ],
        [
            {
                'n': 4,
            },
            [
                '(((())))', '((()()))', '((())())', '((()))()', '(()(()))',
                '(()()())', '(()())()', '(())(())', '(())()()', '()((()))',
                '()(()())', '()(())()', '()()(())', '()()()()',
            ],
        ]
    ])
    def test_generate_parentheses(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.generate_parentheses(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
