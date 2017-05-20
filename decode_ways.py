class Solution(object):
    def num_decodings(self, s):
        if '' == s or s.startswith('0'):
            return 0
        counts = [1, 1]
        for i in range(1, len(s)):
            if '0' == s[i]:
                if s[i - 1] not in '12':
                    return 0
                counts.append(counts[-2])
            elif s[i - 1] == '1':
                counts.append(counts[-1] + counts[-2])
            elif s[i - 1] == '2':
                if s[i] in '123456':
                    counts.append(counts[-1] + counts[-2])
                else:
                    counts.append(counts[-1])
            else:
                counts.append(counts[-1])
        return counts[-1]
