class Solution(object):
    def is_subsequence(self, s, t):
        """
        Check if s is a subsequence of t.
        
        Args:
            s: string
            t: string

        Returns:
            bool

        """
        m = len(s)
        i = 0
        for char in t:
            if i >= m:
                break
            if s[i] == char:
                i += 1
        return i == m
