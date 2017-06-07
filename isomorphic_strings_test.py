from unittest import TestCase

from nose_parameterized import parameterized

from isomorphic_strings import Solution


class TestIsomorphicStrings(TestCase):
    @parameterized.expand([
        [
            {
                's': 'paper',
                't': 'title',
            },
            True,
        ],
        [
            {
                's': 'add',
                't': 'egg',
            },
            True,
        ],
        [
            {
                's': 'foo',
                't': 'bar',
            },
            False,
        ],
        [
            {
                's': 'aa',
                't': 'ab',
            },
            False,
        ],
    ])
    def test_is_isomorphic(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_isomorphic(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
