class Solution:
    def is_palindrome(self, n):
        if type(n) != int:
            raise ValueError
        if n < 0:
            return False
        if n == 0:
            return True
        m = n
        counter = 0
        while m:
            counter += 1
            m //= 10
        m = n
        while m >= 10:
            left = m // 10 ** (counter - 1)
            right = m % 10
            if left != right:
                return False
            m %= 10 ** (counter - 1)
            m //= 10
            counter -= 2
        return True
