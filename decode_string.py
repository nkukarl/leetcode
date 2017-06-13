import re
from string import ascii_letters as LETTERS


class Solution(object):
    def decode_string(self, s):
        if '' == s:
            return ''
        stack = [s[0]]
        for char in s[1:]:
            if ']' == char:
                ss = stack.pop()
                stack.pop()
                count = int(stack.pop())
                ss *= count
                if [] == stack or stack[-1][0] not in LETTERS:
                    stack.append(ss)
                else:
                    stack[-1] += ss
            elif re.match(r'^([a-z]{2,}|\d{2,})$', stack[-1] + char, re.I):
                # char and the last element of stack are both
                # <1> letters or
                # <2> digits
                stack[-1] += char
            else:
                stack.append(char)
        return stack.pop()
