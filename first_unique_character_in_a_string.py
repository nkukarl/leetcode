class Solution(object):
    def first_unique_char(self, s):
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1

        for i, char in enumerate(s):
            if 1 == summary[char]:
                return i

        return -1
