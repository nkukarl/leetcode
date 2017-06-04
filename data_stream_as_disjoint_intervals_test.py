from unittest import TestCase

from data_stream_as_disjoint_intervals import Interval, SummaryRanges


class TestDataStreamAsDisjointIntervals(TestCase):
    def test_summary_ranges(self):
        # Setup
        summary_ranges = SummaryRanges()

        # Exercise and Verify
        summary_ranges.add_num(1)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 1)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

        summary_ranges.add_num(3)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 1), Interval(3, 3)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

        summary_ranges.add_num(8)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 1), Interval(3, 3), Interval(8, 8)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

        summary_ranges.add_num(2)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 3), Interval(8, 8)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

        summary_ranges.add_num(7)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 3), Interval(7, 8)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

        summary_ranges.add_num(5)
        intervals = summary_ranges.get_intervals()
        expected_intervals = [Interval(1, 3), Interval(5, 5), Interval(7, 8)]
        self.assertTrue(self.compare_intervals(intervals, expected_intervals))

    def compare_intervals(self, intervals, expected_intervals):
        if len(intervals) != len(expected_intervals):
            return False
        for intv, exp_intv in zip(intervals, expected_intervals):
            if intv.start != exp_intv.start or intv.end != exp_intv.end:
                return False
        return True