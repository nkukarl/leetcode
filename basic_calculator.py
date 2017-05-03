import string


class Solution(object):
    def calculate(self, s):
        s = s.replace(' ', '')
        if '' == s:
            return 0
        if s.startswith('-'):
            s = '0' + s
        stack = [s[0]]
        for char in s[1:]:
            if char != ')':
                if char in string.digits and stack[-1][0] in string.digits:
                    stack[-1] += char
                else:
                    stack.append(char)
            else:
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop())
                stack.pop()
                stack.append(self._calc(ss[::-1]))
        return self._calc(stack)

    def _calc(self, ss):
        """

        Evaluate string without parentheses.

        Args:
            ss:

        Returns:

        """
        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        ans = int(ss.pop(0))
        while ss != []:
            op = ss.pop(0)
            n = int(ss.pop(0))
            ans = operator[op](ans, n)
        return ans
