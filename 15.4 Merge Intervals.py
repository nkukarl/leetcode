class Interval:
	def __init__(self, start, end):
		self.start, self.end = start, end

class Solution:
	def merge(self, intervals):
		intervals.sort(key = lambda x: x.start)
		ans = [intervals[0]]
		for i in intervals[1:]:
			if i.start <= ans[-1].end:
				ans[-1].end = max(i.end, ans[-1].end)
			else:
				ans.append(i)
		return ans

intervals = [Interval(0, 2), Interval(1, 4), Interval(6, 10), Interval(14, 20), Interval(1, 9)]

inst = Solution()
intervals = inst.merge(intervals)

for i in intervals:
	print(i.start, i.end)