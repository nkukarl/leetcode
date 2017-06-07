class Solution(object):
    def word_pattern(self, pattern, string):
        p = pattern
        s = string.split()

        return len(p) == len(s) and self.check_surjective(p, s) and \
               self.check_surjective(s, p)

    def check_surjective(self, p, s):
        summary = {}
        for pp, ss in zip(p, s):
            if pp in summary:
                if ss != summary[pp]:
                    return False
            else:
                summary[pp] = ss

        return True
