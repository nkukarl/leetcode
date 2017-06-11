from unittest import TestCase

from nose_parameterized import parameterized

from assign_cookies import Solution


class TestAssignCookies(TestCase):
    @parameterized.expand([
        [
            {
                'greed_levels': [1, 2, 3],
                'sizes': [2, 3, 4],
            },
            3,
        ],
        [
            {
                'greed_levels': [1, 2, 3],
                'sizes': [1, 1, 3],
            },
            2,
        ],
        [
            {
                'greed_levels': [1, 2, 3],
                'sizes': [1, 1, 1],
            },
            1,
        ],
    ])
    def test_find_content_children(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_content_children(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
