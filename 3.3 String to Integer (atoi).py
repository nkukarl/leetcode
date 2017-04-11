class Solution:
    def myAtoi(self, s):
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        res = 0
        maxInt = 2 ** 31 - 1
        while i < n:
            if s[i] < '0' or s[i] > '9':
                break
            if res > maxInt // 10 or (
                    res == maxInt and ord(s[i]) - ord('0') > maxInt % 10):
                if sign > 0:
                    return maxInt
                return sign * (maxInt + 1)
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        return res * sign


s = '123'

inst = Solution()
print(inst.myAtoi(s))
