class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        summary = dict()
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if s[i] in summary:
                maxLen = max(maxLen, i - start)
                start = summary[s[i]] + 1
            summary[s[i]] = i
        maxLen = max(maxLen, len(s) - start)
        return maxLen


s = 'qpxrjxkltzy'
s = 'abcdeafghi'

inst = Solution()
print(inst.lengthOfLongestSubstring(s))
