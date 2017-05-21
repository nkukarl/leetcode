class Solution(object):
    def int_to_roman(self, num):
        DICT = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        ans = ''
        for weight in sorted(DICT.keys(), reverse=True):
            if num < weight:
                continue
            count = num // weight
            num %= weight
            ans += count * DICT[weight]
        return ans
