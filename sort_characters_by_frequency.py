class Solution(object):
    def frequency_sort(self, s):
        summary = self.summarise(s)
        stat, stat_keys = self.get_stat(summary)
        res = ''
        for n in stat_keys:
            for c in stat[n]:
                res += c * n
        return res

    def summarise(self, s):
        summary = {}
        for c in s:
            summary[c] = summary.get(c, 0) + 1
        return summary

    def get_stat(self, summary):
        stat = {}
        for c, n in summary.items():
            stat[n] = stat.get(n, []) + [c]
        return stat, sorted(list(stat.keys()), reverse=True)
