class Solution(object):
    def is_isomorphic(self, s, t):
        if len(s) != len(t):
            return False

        summary_s, summary_t = {}, {}
        for ss, tt in zip(s, t):
            if ss in summary_s:
                if tt != summary_s[ss]:
                    return False
            else:
                summary_s[ss] = tt

            if tt in summary_t:
                if ss != summary_t[tt]:
                    return False
            else:
                summary_t[tt] = ss

        return True
