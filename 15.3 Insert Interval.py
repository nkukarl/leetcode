class Interval:
	def __init__(self, start, end):
		self.start, self.end = start, end

class Solution:
	def insert(self, intervals, newInterval):
		left, right = 0, len(intervals)
		if newInterval.start < intervals[0].start:
			intervals.insert(0, newInterval)
		elif newInterval.start > intervals[-1].start:
			intervals.append(newInterval)
		else:
			while left < right:
				mid = (left + right) // 2
				if intervals[mid].start < newInterval.start:
					left = mid + 1
				else:
					right = mid
			intervals.insert(left, newInterval)
		# for i in intervals:
		# 	print(i.start, i.end)
		ans = [intervals[0]]
		for i in intervals[1:]:
			if i.start <= ans[-1].end:
				ans[-1].end = max(i.end, ans[-1].end)
			else:
				ans.append(i)
		return ans

intervals = [Interval(0, 2), Interval(1, 4), Interval(6, 10), Interval(14, 20)]
newInterval = Interval(1, 9)

inst = Solution()
intervals = inst.insert(intervals, newInterval)

for i in intervals:
	print(i.start, i.end)