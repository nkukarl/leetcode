class Solution(object):
    def merge(self, intervals):
        # Handle simple scenario
        if len(intervals) < 2:
            return intervals
        # Handle general scenario
        intervals.sort(key=lambda interval: interval.start)
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start > ans[-1].end:
                ans.append(interval)
            else:
                ans[-1].end = max(ans[-1].end, interval.end)
        return ans
