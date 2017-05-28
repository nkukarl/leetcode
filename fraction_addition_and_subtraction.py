class Solution(object):
    def fraction_addition(self, expression):
        fractions = []
        if not expression.startswith('-'):
            expression = '+' + expression
        fraction = expression[0]
        for char in expression[1:]:
            if char not in ['+', '-']:
                fraction += char
            else:
                fractions.append(self.parse_fraction(fraction))
                fraction = char
        fractions.append(self.parse_fraction(fraction))
        fractions.reverse()
        fraction = fractions.pop()
        while len(fractions) > 0:
            fraction = self.calc(fraction, fractions.pop())

        n, d = fraction
        if 0 == n:
            return '0/1'
        gcd = self.get_gcd(n, d)
        return str(n // gcd) + '/' + str(d // gcd)

    def parse_fraction(self, fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator, denominator

    def calc(self, frac1, frac2):
        n1, d1 = frac1
        n2, d2 = frac2
        n = n1 * d2 + n2 * d1
        d = d1 * d2
        if 0 == n:
            return [0, 1]
        return [n, d]

    def get_gcd(self, m, n):
        if 0 == m % n:
            return n
        return self.get_gcd(n, m % n)
