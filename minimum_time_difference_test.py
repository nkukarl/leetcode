from unittest import TestCase

from nose_parameterized import parameterized

from minimum_time_difference import Solution


class TestMinimumTimeDifference(TestCase):
    @parameterized.expand([
        [
            {
                'time_points': ['00:00', '23:59'],
            },
            1,
        ],
        [
            {
                'time_points': ['23:59', '01:01'],
            },
            62,
        ],
    ])
    def test_find_min_difference(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_min_difference(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
