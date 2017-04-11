RR = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
II = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class Solution:
    def romanToInt(self, s):
        MAP = dict(zip(RR, II))
        tmp = ''
        n = 0
        for char in s:
            if tmp == '':
                tmp = char
            else:
                if MAP[char] <= MAP[tmp]:
                    n += MAP[tmp]
                    tmp = char
                else:
                    n += MAP[tmp + char]
                    tmp = ''
        if tmp:
            n += MAP[tmp]
        return n

    def intToRoman(self, n):
        s = ''
        for i in range(len(II)):
            s += (n // II[i]) * RR[i]
            n %= II[i]
        return s


inst = Solution()
for i in range(1245, 3909, 4):
    s = inst.intToRoman(i)
    n = inst.romanToInt(s)
    print(i, s, n, i - n)
