from unittest import TestCase

from nose_parameterized import parameterized

from non_overlapping_intervals import Solution


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestNonOverlappingIntervals(TestCase):
    @parameterized.expand([
        [
            [[99, 201], [200, 300], [0, 100], [111, 115], [159, 166]],
            1,
        ],
    ])
    def test_erase_overlap_intervals(self, intervals_raw, expected_ans):
        # Setup
        sol = Solution()
        intervals = [Interval(*ir) for ir in intervals_raw]

        # Exercise
        ans = sol.erase_overlap_intervals(intervals)

        # Verify
        self.assertEqual(ans, expected_ans)
