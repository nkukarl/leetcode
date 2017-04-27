class Solution(object):
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        summary = [0] * 26
        for ss, tt in zip(s.lower(), t.lower()):
            summary[ord(ss) - 97] += 1
            summary[ord(tt) - 97] -= 1
        return [0] * 26 == summary
