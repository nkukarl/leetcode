import string


class Solution(object):
    def decode_string(self, s):
        stack = []
        for char in s:
            if [] == stack:
                stack.append(char)
                continue
            if char != ']':
                if (char in string.digits and stack[-1][0] in string.digits) \
                        or (char in string.ascii_lowercase and
                                    stack[-1][0] in string.ascii_lowercase):
                    stack[-1] += char
                else:
                    stack.append(char)
            else:
                s = stack.pop()
                stack.pop()
                count = int(stack.pop())
                s = s * count
                if [] == stack or stack[-1][0] not in string.ascii_lowercase:
                    stack.append(s)
                else:
                    stack[-1] += s
        return ''.join(stack)
