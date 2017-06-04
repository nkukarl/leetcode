class Solution(object):
    def find_right_interval(self, intervals):
        """
        E.g., intervals = [
            [2, 5], [9, 13], [11, 15], [21, 23], [4, 7], [15, 37]
        ]
        summary = {
            None: -1,
            2: 0,
            4: 4,
            9: 1
            11: 2,
            15: 5,
            21: 3,
        }
        start_pos = [2, 4, 9, 11, 15, 21]
        
        For each interval, i.e., intv, take intv.end to do binary search in
        start_pos.
        If intv.end > start_pos[-1], it has no right interval.
            Return start as None, which corresponds to -1.
        Otherwise, use corresponding insert position to get start and 
            use summary to get the index of corresponding index of interval.
        """
        summary, start_pos = {None: -1}, []
        for i, intv in enumerate(intervals):
            summary[intv.start] = i
            start_pos.append(intv.start)

        start_pos.sort()

        ans = []
        for intv in intervals:
            pos = intv.end
            index = self.find_start(start_pos, pos)
            ans.append(summary[index])

        return ans

    def find_start(self, start_pos, pos):
        if 0 == len(start_pos) or pos > start_pos[-1]:
            return None
        if pos <= start_pos[0]:
            return 0
        left, right = 0, len(start_pos) - 1
        while left < right:
            mid = (left + right) // 2
            if start_pos[mid] < pos:
                left = mid + 1
            else:
                right = mid
        return start_pos[left]
