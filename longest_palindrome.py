class Solution(object):
    def longest_palindrome(self, s):
        summary = {}
        ans = 0
        for char in s:
            if char not in summary:
                summary[char] = 1
            else:
                ans += 2
                summary.pop(char)

        if summary:
            ans += 1

        return ans
