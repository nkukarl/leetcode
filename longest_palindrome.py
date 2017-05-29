class Solution(object):
    def longest_palindrome(self, s):
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1

        flag = False
        ans = 0
        for char in summary:
            if summary[char] % 2 != 0:
                if not flag:
                    ans += summary[char]
                    flag = True
                else:
                    ans += summary[char] - 1
            else:
                ans += summary[char]
        return ans
