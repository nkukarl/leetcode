class Solution(object):
    def erase_overlap_intervals(self, intervals):
        # Handle simple scenario
        if len(intervals) < 2:
            return 0

        intervals = sorted(intervals, key=lambda intv: intv.end)
        end = intervals[0].end
        ans = 0
        for intv in intervals[1:]:
            if intv.start >= end:
                end = intv.end
            else:
                ans += 1
        return ans
