from unittest import TestCase

from nose_parameterized import parameterized

from simplify_path import Solution


class TestSimplifyPath(TestCase):
    @parameterized.expand([
        [
            {
                'path': '/home/',
            },
            '/home',
        ],
        [
            {
                'path': '/a/./b/../../c/',
            },
            '/c',
        ],
    ])
    def test_simplify_path(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.simplify_path(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
