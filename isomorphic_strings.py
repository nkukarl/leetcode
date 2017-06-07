class Solution(object):
    def is_isomorphic(self, s, t):
        if len(s) != len(t):
            return False

        return self.check_surjective(s, t) and self.check_surjective(t, s)

    def check_surjective(self, s, t):
        summary = {}
        for ss, tt in zip(s, t):
            if ss in summary:
                if tt != summary[ss]:
                    return False
            else:
                summary[ss] = tt

        return True
