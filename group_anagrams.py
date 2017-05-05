class Solution(object):
    def group_anagrams(self, strs):
        groups = {}
        for s in strs:
            summary = self.summarise(s)
            groups[summary] = groups.get(summary, []) + [s]
        return groups.values()

    def summarise(self, s):
        # Summarise a string using the counts of each letter
        summary = [0] * 26
        for char in s:
            summary[ord(char) - ord('a')] += 1
        # Convert summary into a tuple so that it is hashable
        return tuple(summary)
