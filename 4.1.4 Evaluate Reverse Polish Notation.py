class Solution:
    def evalRPN(self, s):
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in s:
            if token not in ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    if a * b > 0:
                        sign = 1
                    else:
                        sign = -1
                    stack.append(sign * abs(a) // abs(b))
        return stack[0]


s = ['2', '1', '+', '3', '*']
s = ['4', '13', '5', '/', '+']

inst = Solution()
print(inst.evalRPN(s))
