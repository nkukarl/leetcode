class Solution(object):
    def get_hint(self, secret, guess):
        a_count = 0
        ss = {}
        gg = []
        for s, g in zip(secret, guess):
            if s == g:
                a_count += 1
            else:
                ss[s] = ss.get(s, 0) + 1
                gg.append(g)

        b_count = 0
        for g in gg:
            if ss.get(g, 0) > 0:
                ss[g] -= 1
                b_count += 1

        return '{0}A{1}B'.format(a_count, b_count)
