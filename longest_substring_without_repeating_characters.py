class Solution(object):
    def length_of_longest_substring(self, s):
        summary = {}
        max_count = 0
        left = 0
        for i, char in enumerate(s):
            if char in summary:
                index = summary[char]
                for j in range(left, index + 1):
                    summary.pop(s[j])
                left = index + 1
            summary[char] = i
            count = len(summary)
            max_count = max(max_count, count)
        return max_count
