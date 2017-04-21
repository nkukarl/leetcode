class Solution(object):
    def find_the_difference(self, s, t):
        summary_s = self.summarise(s)
        summary_t = self.summarise(t)
        for c, n in summary_t.items():
            if n != summary_s.get(c, 0):
                return c

    def summarise(self, s):
        summary = {}
        for c in s:
            summary[c] = summary.get(c, 0) + 1
        return summary
