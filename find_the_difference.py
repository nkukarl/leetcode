class Solution(object):
    def find_the_difference(self, s, t):
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1
        for char in t:
            if 0 == summary.get(char, 0):
                return char
            summary[char] -= 1

    def find_the_difference_xor(self, s, t):
        xor = 0
        for char in s + t:
            xor ^= ord(char)
        return chr(xor)
