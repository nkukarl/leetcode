class Solution(object):
    def is_valid(self, s):
        stack = []
        left = {0: '(', 1: '[', 2: '{'}
        right = {')': 0, ']': 1, '}': 2}
        for char in s:
            if char in right:
                if len(stack) > 0 and stack[-1] == left[right[char]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return [] == stack
