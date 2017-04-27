class Solution(object):
    def find_anagrams(self, s, word):
        if len(s) < len(word):
            return []
        summary_w = self.summarise(word)
        summary_s = self.summarise(s[:len(word)])
        diff = [sw - ss for sw, ss in zip(summary_w, summary_s)]
        if not any(diff):
            indices = [0]
        else:
            indices = []
        for i in range(len(s) - len(word)):
            old = s[i]
            new = s[i + len(word)]
            diff[ord(old) - ord('a')] += 1
            diff[ord(new) - ord('a')] -= 1
            if not any(diff):
                indices.append(i + 1)
        return indices

    def summarise(self, s):
        summary = [0] * 26
        for ss in s:
            summary[ord(ss) - ord('a')] += 1
        return summary
