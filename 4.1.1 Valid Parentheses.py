class Solution:
    def isValid(self, s):
        MAP = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in MAP.values():
                stack.append(char)
            else:
                if stack and stack[-1] == MAP[char]:
                    stack.pop()
                else:
                    return False
        return stack == []


s = '([{}()])'
s = ')'
s = '([]'
s = '(())'

inst = Solution()
print(inst.isValid(s))
