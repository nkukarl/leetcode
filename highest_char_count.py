class Solution(object):
    def get_highest_char_count(self, s):
        summary = {}
        max_count = 0
        for ss in s:
            summary[ss] = summary.get(ss, 0) + 1
            max_count = max(max_count, summary[ss])

        return max_count
