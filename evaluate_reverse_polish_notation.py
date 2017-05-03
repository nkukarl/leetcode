class Solution(object):
    def eval_rpn(self, tokens):
        stack = []
        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: abs(x) // abs(y) * (1 if x * y > 0 else -1),
        }
        for t in tokens:
            if t in operator:
                second = stack.pop()
                first = stack.pop()
                f = operator[t]
                stack.append(f(first, second))
            else:
                stack.append(int(t))
        return stack[0] if stack != [] else 0
