class Solution(object):
    def roman_to_int(self, s):
        DICT = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        prev = ''
        ans = 0
        for cur in s:
            if '' == prev:
                prev = cur
                continue
            if DICT[prev] >= DICT[cur]:
                ans += DICT[prev]
                prev = cur
            else:
                ans += DICT[prev + cur]
                prev = ''
        if prev != '':
            ans += DICT[prev]
        return ans
