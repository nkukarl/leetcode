class Solution(object):
    def find_anagrams(self, s, word):
        # Handle simple scenario
        if len(s) < len(word):
            return []
        # Summary word and first len(word) characters of s
        summary_w = self.summarise(word)
        summary_s = self.summarise(s[:len(word)])
        # Initialise diff
        diff = [sw - ss for sw, ss in zip(summary_w, summary_s)]
        # Check if there is any number other than 0 in diff
        if not any(diff):
            # word and first len(word) characters of s are anagrams
            indices = [0]
        else:
            indices = []
        # Traverse remaining characters of s
        for i in range(len(s) - len(word)):
            # Update diff when traversing
            old = s[i]
            new = s[i + len(word)]
            diff[ord(old) - ord('a')] += 1
            diff[ord(new) - ord('a')] -= 1
            # Note down indices of interest
            if not any(diff):
                indices.append(i + 1)
        return indices

    def summarise(self, s):
        """

        Summarise a string using a list of integers representing
        the number of each character.

        E.g., s = 'aaabbccccdee'
        Return [3, 2, 4, 1, 2, 0, ..., 0]

        """
        summary = [0] * 26
        for ss in s:
            summary[ord(ss) - ord('a')] += 1
        return summary
