class Solution:
    def lengthOfLastWord(self, s):
        s = s.split()
        if not s:
            return -1
        return len(s[-1])
