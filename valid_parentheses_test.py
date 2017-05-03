from unittest import TestCase

from nose_parameterized import parameterized

from valid_parentheses import Solution


class TestValidParentheses(TestCase):
    @parameterized.expand([
        [
            {
                's': '{}[][]()'
            },
            True,
        ],
        [
            {
                's': '{}[{[()]}][]()'
            },
            True,
        ],
        [
            {
                's': '{}[][[[()()]]()[]]()'
            },
            True,
        ],
        [
            {
                's': ''
            },
            True,
        ],
        [
            {
                's': '(('
            },
            False,
        ],
        [
            {
                's': ')'
            },
            False,
        ],
        [
            {
                's': '{}[][](()'
            },
            False,
        ],
        [
            {
                's': '{{}][][]()'
            },
            False,
        ],
    ])
    def test_is_valid(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_valid(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
