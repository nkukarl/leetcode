from unittest import TestCase

from nose_parameterized import parameterized

from sliding_window_maximum import Solution


class TestSlidingWindowMaximum(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [],
                'k': 0,
            },
            [],
        ],
        [
            {
                'nums': [1, 3, -1, -3, 5, 3, 6, 7],
                'k': 3,
            },
            [3, 3, 5, 5, 6, 7],
        ],
        [
            {
                'nums': [7, 2, 4],
                'k': 2,
            },
            [7, 4],
        ],
    ])
    def test_max_sliding_window(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_sliding_window(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
