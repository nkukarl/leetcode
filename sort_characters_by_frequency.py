class Solution(object):
    def frequency_sort(self, s):
        # Summarise s to get char: count as key: value pairs.
        summary_raw = {}
        for char in s:
            summary_raw[char] = summary_raw.get(char, 0) + 1

        # Each element is a pair of count and char
        summary = [(v, k) for k, v in summary_raw.items()]

        # Characters with low frequency will come first, hence when building
        # ans, we should pop from summary.
        summary.sort()

        ans = ''
        while summary:
            count, char = summary.pop()
            ans += char * count

        return ans
