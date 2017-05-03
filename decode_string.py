import re
from string import ascii_lowercase as LETTERS


class Solution(object):
    def decode_string(self, s):
        if '' == s:
            return ''
        stack = [s[0]]
        for char in s[1:]:
            if char != ']':
                # char and the last element of stack are both
                # <1> lowercase letters or
                # <2> digits
                if re.match(r'^([a-z]{2,}|\d{2,})$', stack[-1] + char):
                    stack[-1] += char
                else:
                    stack.append(char)
            else:
                ss = stack.pop()
                stack.pop()
                count = int(stack.pop())
                ss = ss * count
                if [] == stack or stack[-1][0] not in LETTERS:
                    stack.append(ss)
                else:
                    stack[-1] += ss
        return stack[0]
