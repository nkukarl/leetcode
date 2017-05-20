from unittest import TestCase

from nose_parameterized import parameterized

from merge_intervals import Solution


class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


class TestMergeIntervals(TestCase):
    @parameterized.expand([
        [
            {
                'intervals': [
                    Interval(8, 10), Interval(15, 18),
                    Interval(1, 3), Interval(2, 6),
                ],
            },
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)],
        ],
        [
            {
                'intervals': [],
            },
            [],
        ],
        [
            {
                'intervals': [Interval(1, 5)],
            },
            [Interval(1, 5)],
        ],
    ])
    def test_merge(self, kwargs, expected_intervals):
        # Setup
        sol = Solution()

        # Exercise
        intervals = sol.merge(**kwargs)

        # Verify
        for interval, expected_interval in zip(intervals, expected_intervals):
            self.assertEqual(
                (interval.start, interval.end),
                (expected_interval.start, expected_interval.end),
            )
