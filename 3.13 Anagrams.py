class Solution:
    def anagrams(self, strs):
        summary = dict()
        for s in strs:
            tmp = ''.join(sorted(list(s)))
            summary[tmp] = summary.get(tmp, []) + [s]
        res = []
        for v in summary.values():
            if len(v) >= 2:
                res.append(v)
        return res


strs = ['abc', 'cde', 'bca', 'dec', 'ced', 'aa']

inst = Solution()
print(inst.anagrams(strs))
