class Solution(object):
    def find_anagrams(self, s, word):
        if len(s) < len(word):
            return []
        self.summary_word = self.summarise(word)
        indices = []
        valid_anagrams = {word}
        invalid_anagrams = set()
        for i in range(len(s) - len(word) + 1):
            ss = s[i: i + len(word)]
            if ss in invalid_anagrams:
                continue
            if ss in valid_anagrams:
                indices.append(i)
                continue
            if self.is_anagram(ss):
                valid_anagrams.add(ss)
                indices.append(i)
            else:
                invalid_anagrams.add(ss)
        return indices

    def summarise(self, s):
        summary = [0] * 26
        for ss in s:
            summary[ord(ss) - 97] += 1
        return summary

    def is_anagram(self, t):
        summary_t = self.summarise(t)
        diff = [w - t for w, t in zip(self.summary_word, summary_t)]
        return not any(diff)
