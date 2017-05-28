class Solution(object):
    def first_unique_char(self, s):
        chars = set()
        duplicates = set()
        for char in s:
            if char not in chars:
                chars.add(char)
            else:
                duplicates.add(char)

        for i, char in enumerate(s):
            if char not in duplicates:
                return i
        return -1
