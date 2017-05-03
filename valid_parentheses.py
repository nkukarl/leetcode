class Solution(object):
    def is_valid(self, s):
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
        return [] == stack
