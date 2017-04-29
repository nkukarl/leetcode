class Solution(object):
    def fraction_to_decimal(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        ratio, remainder = divmod(numerator, denominator)
        integer = sign + str(ratio)
        if 0 == remainder:
            return integer
        cache = []
        decimals = []
        while remainder not in cache:
            cache.append(remainder)
            ratio, remainder = divmod(remainder * 10, denominator)
            decimals.append(str(ratio))
        index_ = cache.index(remainder)
        decimals.insert(index_, '(')
        decimals.append(')')
        return integer + '.' + ''.join(decimals).replace('(0)', '')
