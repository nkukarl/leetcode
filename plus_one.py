class Solution:
    def plus_one(self, digits):
        carry = 1
        n = len(digits)
        i = n - 1
        while carry and i >= 0:
            result = digits[i] + carry
            carry = result // 10
            digits[i] = result % 10
            i -= 1
        if 1 == carry:
            digits.insert(0, 1)
