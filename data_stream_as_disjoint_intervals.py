class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class SummaryRanges(object):
    def __init__(self):
        self.nums = set()
        self.intervals = []

    def addNum(self, val):
        self.add_num(val)

    def add_num(self, val):
        if val in self.nums:
            return
        self.nums.add(val)
        intv = Interval(val, val)
        # Handle simple scenarios
        # <1> self.intervals is empty
        if 0 == len(self.intervals):
            self.intervals.append(intv)
            return
        # <2> val is smaller than the start of the first interval
        if val < self.intervals[0].start:
            if val + 1 in self.nums:
                self.intervals[0].start = val
            else:
                self.intervals.insert(0, intv)
            return
        # <3> val is greater than the end of the last interval
        if val > self.intervals[-1].end:
            if val - 1 in self.nums:
                self.intervals[-1].end = val
            else:
                self.intervals.append(intv)
            return

        # Binary search
        left, right = 0, len(self.intervals) - 1
        while left < right:
            mid = (left + right) // 2
            if val > self.intervals[mid].start:
                left = mid + 1
            else:
                right = mid
        pos = left
        # If mergeable from both sides
        if val - 1 in self.nums and val + 1 in self.nums:
            self.intervals[pos - 1].end = self.intervals.pop(pos).end
        # If mergeable from left side
        elif val - 1 in self.nums:
            self.intervals[pos - 1].end = val
        # If mergeable from right side
        elif val + 1 in self.nums:
            self.intervals[pos].start = val
        # Not mergeable from both sides
        else:
            self.intervals.insert(pos, intv)

    def getIntervals(self):
        return self.get_intervals()

    def get_intervals(self):
        return self.intervals
