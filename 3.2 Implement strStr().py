class Solution:
    def strStr(self, s, t):
        for i in range(len(s) - len(t) + 1):
            tmp = ''
            ii = i
            j = 0
            while j < len(t) and s[ii] == t[j]:
                tmp += t[j]
                ii += 1
                j += 1
            if tmp == t:
                return i
        return -1


s, t = 'password', 'wor'

inst = Solution()
print(inst.strStr(s, t))
