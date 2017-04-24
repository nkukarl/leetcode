class Solution(object):
    def convert_to_base_7(self, num):
        if 0 == num:
            return '0'
        sign = ''
        if num < 0:
            sign = '-'
        num = abs(num)
        base = 1
        power = 0
        while num >= base:
            base *= 7
            power += 1
        base //= 7
        ans_raw = ['0'] * power
        for i in range(power):
            ans_raw[i] = str(num // base)
            num = num % base
            if 0 == num:
                break
            base //= 7
        return sign + ''.join(ans_raw)
